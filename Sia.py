
import os



print('     Escola a FERRAMENTA\n')
print(' 1 - AudioX (Sonorizador) \n2 - tortoise-tts (Gerador de voz) \n 2 - TTS (Texto pra fala)\n 3 - ComfyUI  (Ia image)\n 4 - Focuus (Ia image)')


op = input('Escolha uma opção: ')    
try:
    int(op)
except:
    op = input('Opção invalida, digite novamente: ')



if op == "1":
    os.system("git clone https://github.com/Kireyarck/AudioX.git" )
    os.system("conda create -n AudioX python=3.8.20")
    os.system("conda activate AudioX")
    os.system("pip install git+https://github.com/ZeyueT/AudioX.git")
    os.system("conda install -c conda-forge ffmpeg libsndfile")
    os.system('python3 AudioX/run_gradio.py --model-config model/config.json --share')

if op == "2":
    os.system("conda create --name tortoise python=3.9 numba inflect" )
    os.system("conda activate tortoise")
    os.system("conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia")
    os.system("conda install transformers=4.29.2")
    os.system("git clone https://github.com/neonbjb/tortoise-tts.git")
    os.system('python3 tortoise-tts/setup.py install')
    
