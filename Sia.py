
import os



print('     Escola a FERRAMENTA\n')
print(' 1 - AudioX (Sonorizador) \n2 - tortoise-tts (Gerador de voz) \n 2 - TTS (Texto pra fala)\n 3 - ComfyUI  (Ia image)\n 4 - Focuus (Ia image)')


op = input('Escolha uma opção: ')


    
    
try:
    int(op)
except:
    op = input('Opção invalida, digite novamente: ')



if op == 1:
    print(op)
    os.system("git clone https://github.com/Kireyarck/AudioX.git" )
    os.system("conda create -n AudioX python=3.8.20")
    os.system("conda activate AudioX")
    os.system("pip install git+https://github.com/ZeyueT/AudioX.git")
    os.system("conda install -c conda-forge ffmpeg libsndfile")
