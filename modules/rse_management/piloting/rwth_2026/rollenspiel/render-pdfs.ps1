<#
.SYNOPSIS
    Rendert das Rollenspiel und exportiert jede Seite als eigenständiges PDF.
    Unterstützt Deutsch (-Lang de, Default) und Englisch (-Lang en).

.DESCRIPTION
    1. `quarto render --profile print` (bzw. `--profile print-en`) im Repo-Root
       -> erzeugt die Rollenspiel-Seiten nach _site-print/ (bzw. _site-print-en/)
       unter .../rollenspiel/*.html (inkl. karten/rolle-*.html). Nur diese
       Seiten werden gerendert, nicht die ganze Curriculum-Site. Die englische
       Fassung liegt unter .../rollenspiel/en/.
    2. Druckt jede HTML-Seite via Headless-Browser (Edge oder Chrome) nach
       pdf/*.pdf (de) bzw. pdf-en/*.pdf (en). Die PDFs nutzen die
       @media-print-Regeln aus styles.css (Navbar/Sidebar aus, Karten sauber
       umbrochen) -- deshalb Browser-Druck statt LaTeX: die CSS-Karten bleiben
       so erhalten.
    3. Packt Bundles nach dist/:
         student[-en].zip  = NUR die gemeinsamen, geheimnisfreien Handouts
                             (Szenario + öffentliche Rollen-Übersicht).
         teacher[-en].zip  = ALLES (inkl. aller geheimer Einzelkarten,
                             Ereignisse/Timeline und Spielleitungs-Übersicht).
    4. Mit -Publish werden die für die OER-Seite verlinkten Handouts in
       handouts/ (de) bzw. handouts/en/ (en) unter ihren finalen Namen
       (rollenspiel-*.pdf / rollenspiel-*-paket.zip) abgelegt.

    HINWEIS ZUM VERHANDLUNGSTRAINING:
       Die 5 vertraulichen Einzel-Rollenkarten liegen einzeln als
       pdf/rolle-*.pdf vor. Sie kommen bewusst NICHT in student.zip -- die
       Spielleitung verteilt sie 1:1 (jede:r sieht nur die eigene Karte).

.PARAMETER Lang
    Sprache: 'de' (Default) oder 'en'. Wählt Profil, Ausgabeordner und
    Bundle-/Handout-Namen.

.PARAMETER SkipRender
    Überspringt `quarto render` und nutzt die vorhandenen _site-print*/*.html.

.PARAMETER Publish
    Kopiert die Handout-PDFs und Bundles unter ihren finalen Namen nach
    handouts/ (de) bzw. handouts/en/ (en).

.PARAMETER Browser
    Optionaler Pfad zu msedge.exe / chrome.exe (sonst Auto-Erkennung).

.EXAMPLE
    ./render-pdfs.ps1                     # deutsche PDFs + Bundles
    ./render-pdfs.ps1 -Lang en            # englische PDFs + Bundles
    ./render-pdfs.ps1 -Lang en -Publish   # englisch, nach handouts/en/ ablegen
    ./render-pdfs.ps1 -SkipRender
#>
param(
    [ValidateSet('de', 'en')]
    [string]$Lang = 'de',
    [switch]$SkipRender,
    [switch]$Publish,
    [string]$Browser
)

$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
# Repo-Wurzel: fünf Ebenen über diesem Ordner
# (modules/rse_management/piloting/rwth_2026/rollenspiel -> Repo-Root).
$repoRoot = (Resolve-Path (Join-Path $root '..\..\..\..\..')).Path

# Sprachspezifische Konfiguration ---------------------------------------------
$rsSub = 'modules\rse_management\piloting\rwth_2026\rollenspiel'
if ($Lang -eq 'en') {
    $profileName = 'print-en'
    $siteRoot    = '_site-print-en'
    $siteSub     = Join-Path $rsSub 'en'
    $pdfDir      = Join-Path $root 'pdf-en'
    $studentZip  = 'student-en'
    $teacherZip  = 'teacher-en'
    $handoutDir  = Join-Path $root 'handouts\en'
} else {
    $profileName = 'print'
    $siteRoot    = '_site-print'
    $siteSub     = $rsSub
    $pdfDir      = Join-Path $root 'pdf'
    $studentZip  = 'student'
    $teacherZip  = 'teacher'
    $handoutDir  = Join-Path $root 'handouts'
}
# Ausgabe des Print-Profils; die Seiten liegen dort unter ihrem Projektpfad.
$siteDir = Join-Path (Join-Path $repoRoot $siteRoot) $siteSub
$distDir = Join-Path $root 'dist'

# Seiten: src = Pfad unter _site (ohne .html), out = PDF-Basisname ------------
$pages = @(
    @{ src = 'index';               out = 'index'             },
    @{ src = 'szenario';            out = 'szenario'          },
    @{ src = 'rollen-oeffentlich';  out = 'rollen-oeffentlich' },
    @{ src = 'rollenkarten';        out = 'verteilung'        },
    @{ src = 'karten/rolle-1-rse';     out = 'rolle-1-rse'     },
    @{ src = 'karten/rolle-2-pi';      out = 'rolle-2-pi'      },
    @{ src = 'karten/rolle-3-domaene'; out = 'rolle-3-domaene' },
    @{ src = 'karten/rolle-4-hiwi';    out = 'rolle-4-hiwi'    },
    @{ src = 'karten/rolle-5-schule';  out = 'rolle-5-schule'  },
    @{ src = 'ereigniskarten';      out = 'ereignisse'        },
    @{ src = 'spielleitung';        out = 'spielleitung'      }
)

# student.zip: NUR geheimnisfreie, gemeinsame Handouts fuer ALLE.
# (Die Einzelkarten rolle-*.pdf werden 1:1 verteilt, nicht gebuendelt.
#  Die Verteil-Handreichung 'verteilung' ist Spielleitungs-Material -> nur teacher.zip.)
$studentOut = @('szenario', 'rollen-oeffentlich')

# teacher.zip: alles.
$teacherOut = $pages | ForEach-Object { $_.out }

# Publish-Zuordnung: welches PDF/Bundle unter welchem finalen Handout-Namen.
$publishPdf = @(
    @{ out = 'szenario';           to = 'rollenspiel-szenario.pdf'       },
    @{ out = 'rollen-oeffentlich'; to = 'rollenspiel-rollen-handout.pdf' },
    @{ out = 'verteilung';         to = 'rollenspiel-verteilung.pdf'     },
    @{ out = 'spielleitung';       to = 'rollenspiel-spielleitung.pdf'   }
)
$publishZip = @(
    @{ zip = $studentZip; to = 'rollenspiel-teilnehmer-paket.zip'   },
    @{ zip = $teacherZip; to = 'rollenspiel-spielleitung-paket.zip' }
)

Write-Host "==> Sprache: $Lang (Profil $profileName)" -ForegroundColor Cyan

# 1. Rendern -------------------------------------------------------------------
if (-not $SkipRender) {
    Write-Host "==> quarto render --profile $profileName" -ForegroundColor Cyan
    Push-Location $repoRoot
    try { quarto render --profile $profileName } finally { Pop-Location }
    if ($LASTEXITCODE -ne 0) { throw "quarto render --profile $profileName schlug fehl (Exit $LASTEXITCODE)" }
} else {
    Write-Host '==> quarto render uebersprungen (-SkipRender)' -ForegroundColor Yellow
}

# 2. Browser finden ------------------------------------------------------------
if (-not $Browser) {
    $candidates = @(
        "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe",
        "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe",
        "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
        "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe"
    )
    $Browser = $candidates | Where-Object { Test-Path $_ } | Select-Object -First 1
}
if (-not $Browser -or -not (Test-Path $Browser)) {
    throw "Kein Headless-Browser (Edge/Chrome) gefunden. Pfad via -Browser angeben."
}
Write-Host "==> Browser: $Browser" -ForegroundColor Cyan

# 3. PDFs drucken --------------------------------------------------------------
if (Test-Path $pdfDir) { Remove-Item $pdfDir -Recurse -Force }
New-Item -ItemType Directory -Path $pdfDir | Out-Null

foreach ($p in $pages) {
    $html = Join-Path $siteDir ("$($p.src).html")
    if (-not (Test-Path $html)) { Write-Warning "fehlt: $html -- uebersprungen"; continue }
    $pdf     = Join-Path $pdfDir "$($p.out).pdf"
    $fileUrl = 'file:///' + ($html -replace '\\', '/')
    $tmpProf = Join-Path $env:TEMP ("ls-pdf-" + $Lang + "-" + $p.out)
    $logOut  = Join-Path $env:TEMP ("ls-pdf-" + $Lang + "-" + $p.out + ".out")
    $logErr  = Join-Path $env:TEMP ("ls-pdf-" + $Lang + "-" + $p.out + ".err")

    # Argumente einzeln zusammensetzen; Pfade mit Sonderzeichen werden gequotet.
    # Start-Process statt & : haelt den (harmlosen) Browser-stderr aus dem
    # PowerShell-Fehlerstrom -- sonst bricht $ErrorActionPreference='Stop' ab.
    $browserArgs = @(
        '--headless=new', '--disable-gpu', '--no-first-run', '--no-sandbox',
        '--no-pdf-header-footer',
        '--virtual-time-budget=8000', '--run-all-compositor-stages-before-draw',
        ('"--user-data-dir={0}"' -f $tmpProf),
        ('"--print-to-pdf={0}"'  -f $pdf),
        ('"{0}"' -f $fileUrl)
    )

    Write-Host "    -> $($p.out).pdf"
    $proc = Start-Process -FilePath $Browser -ArgumentList $browserArgs `
        -Wait -NoNewWindow -PassThru `
        -RedirectStandardOutput $logOut -RedirectStandardError $logErr

    foreach ($f in @($tmpProf, $logOut, $logErr)) {
        if (Test-Path $f) { Remove-Item $f -Recurse -Force -ErrorAction SilentlyContinue }
    }
    if (-not (Test-Path $pdf) -or (Get-Item $pdf).Length -eq 0) {
        throw "PDF-Export fuer $($p.out) fehlgeschlagen (Browser-Exit $($proc.ExitCode))."
    }
}

# 4. Bundeln -------------------------------------------------------------------
if (-not (Test-Path $distDir)) { New-Item -ItemType Directory -Path $distDir | Out-Null }

function New-Bundle {
    param([string]$Name, [string[]]$Outs)
    $files = $Outs | ForEach-Object { Join-Path $pdfDir "$_.pdf" } | Where-Object { Test-Path $_ }
    $zip = Join-Path $distDir "$Name.zip"
    if (Test-Path $zip) { Remove-Item $zip -Force }
    Compress-Archive -Path $files -DestinationPath $zip -Force
    Write-Host ("==> {0,-16} {1} PDF(s) -> {2}" -f "$Name.zip", $files.Count, $zip) -ForegroundColor Green
}

New-Bundle -Name $studentZip -Outs $studentOut
New-Bundle -Name $teacherZip -Outs $teacherOut

# 5. Publish (optional) --------------------------------------------------------
if ($Publish) {
    if (-not (Test-Path $handoutDir)) { New-Item -ItemType Directory -Path $handoutDir -Force | Out-Null }
    Write-Host "==> Publish nach $handoutDir" -ForegroundColor Cyan
    foreach ($m in $publishPdf) {
        $srcPdf = Join-Path $pdfDir "$($m.out).pdf"
        if (Test-Path $srcPdf) {
            Copy-Item $srcPdf (Join-Path $handoutDir $m.to) -Force
            Write-Host "    -> $($m.to)"
        }
    }
    foreach ($m in $publishZip) {
        $srcZip = Join-Path $distDir "$($m.zip).zip"
        if (Test-Path $srcZip) {
            Copy-Item $srcZip (Join-Path $handoutDir $m.to) -Force
            Write-Host "    -> $($m.to)"
        }
    }
}

Write-Host ''
Write-Host 'Fertig.' -ForegroundColor Green
Write-Host "  Einzel-PDFs      : $pdfDir"
Write-Host "  Vertrauliche Karten (1:1 verteilen): rolle-1-rse.pdf ... rolle-5-schule.pdf"
Write-Host "  Bundles          : $distDir\$studentZip.zip (nur Szenario+Uebersicht) , $distDir\$teacherZip.zip (alles)"
if ($Publish) { Write-Host "  Handouts         : $handoutDir" }
