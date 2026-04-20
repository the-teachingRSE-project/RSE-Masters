cd generation || exit

python generate_all.py --profile cs
python generate_all.py --profile mnt
python generate_all.py --profile up

cd ..

