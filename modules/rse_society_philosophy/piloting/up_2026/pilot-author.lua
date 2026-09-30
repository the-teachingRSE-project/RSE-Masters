-- Setzt pilot-author (siehe _metadata.yml) als einzige Autorschaft.
-- Quarto hängt author-Listen aus _quarto.yml und _metadata.yml aneinander und hat sie schon
-- zu authors / by-author normalisiert, wenn dieser Filter läuft. Darum werden alle drei
-- Felder hier aus pilot-author neu gesetzt.
local stringify = pandoc.utils.stringify

local function normalized(entry, i)
  local n = {}
  for k, v in pairs(entry) do n[k] = v end
  n.name = { literal = entry.name }
  n.id = tostring(i)
  n.number = tostring(i)
  return n
end

function Meta(meta)
  local pilot = meta["pilot-author"]
  if not pilot then return nil end
  local norm = pandoc.List()
  for i, a in ipairs(pilot) do norm:insert(normalized(a, i)) end
  meta.author = pilot
  meta.authors = norm
  meta["by-author"] = norm
  meta["author-meta"] = table.concat(pilot:map(function(a) return stringify(a.name) end), "; ")
  meta["pilot-author"] = nil
  return meta
end
