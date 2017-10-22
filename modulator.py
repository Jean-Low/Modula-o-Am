import soundfile as sf
import sounddevice as sd
import os
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftshift
from scipy import signal as sg



class Noiszes: 

    def __init__(self):

            self.fs = 44100
            self.wav = None

    def playSound(self,sound,looping = False, wait = True):
            print("playing audio")
            sd.play(sound, self.fs, loop = looping)
            if(wait):
                sd.wait()

    def calcFFT(self,signal, fs):
        # https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
        #y  = np.append(signal, np.zeros(len(signal)*fs))
        N  = len(signal)
        T  = 1.0/fs
        print("AAAAA")
        print(signal[0])
        print(len(signal))
        print(T)
        xf = np.linspace(-1.0/(2.0*T), 1.0/(2.0*T), N)
        print("AZUL")
        yf = fft(signal)
        print("AZULado")
        return(xf, fftshift(yf))

    def gravar(self, tempo):
            audio = sd.rec(int(tempo*self.fs), self.fs, channels=1)
            sd.wait()
            self.wav = audio
            self.fs = audio[1]  
            audio = audio[:,0]
            return audio
    
    def LPF(self,signal, cutoff_hz, fs):
            #####################
            # Filtro
            #####################
            # https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html
            nyq_rate = fs/2
            width = 5.0/nyq_rate
            ripple_db = 60.0 #dB
            N , beta = sg.kaiserord(ripple_db, width)
            taps = sg.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
            return( sg.lfilter(taps, 1.0, signal))
        

    def Modular(self, audio):
            print("AHOIZ")




    #isto transforma uma lista em .wav
    def escrever(self, nome_do_arquivo, som):
            sf.write('Saves/' + nome_do_arquivo + ".wav", som, self.fs)
            print("o destino foi escrito")     


    def main(self):
        print('\nO que deseja fazer?\n1- Gravar um audio\n2- Carregar um audio')
        choice = input()
        print(choice)
        if(choice == '1'):
            print('Vamos gravar um Audio!')
            print('Quantos segundos vamos gravar?')
            audio = self.gravar(int(input()))
            print('\nGravado!\nAgora o que deseja fazer?')
        elif(choice == '2'):
            print('Os seguintes arquivos foram encontrados:')
            fileList = []
            count = 0
            for i in sorted(os.listdir('Saves')):
                


                print(str(count) + ' - ' + i)
                fileList.append(i)
                count+= 1

            while(True):
                print('Escolha o arquivo: (Sem o .wav)')
                choice = input()
                try:
                    try:
                        print("\nLOADING BY INDEX")
                        self.wav, self.fs= sf.read("Saves/" + fileList[int(choice)]);
                        audio = self.wav[:,0]
                    except:
                        self.wav, self.fs = sf.read("Saves/" + choice + ".wav");
                        audio = self.wav[:,0]
                    print('\nCarregado!\nAgora o que deseja fazer?')
                    break
                except:
                    print('arquivo requisitado nao existe!!!\n')
        else:
            print('Opa, algo esta errado com sua escolha!')
            return
        while(True):
            print('1- Salvar\n2- Reproduzir \n3- plotar grafico \n4- Modularizar\n 5- Tentar novamente')
            choice = input()
            if(choice == '1'):
                print("Com qual nome devemos gravar")
                name = input()
                self.escrever(name, audio)
                print("Salvo como: " + name )
            elif(choice == '2'):
                print("Reproduzindo")
                self.playSound(audio, wait = False)
                print("Para parar aperte ENTER" )
                input()
                sd.stop()
            elif(choice == '3'):
                print('\nAplicar transformada de fourier ? (Y ou N)')
                ft = input()
                if(ft == 'y'):
                    fftAudio = self.calcFFT(audio, self.fs)
                    print(fftAudio)
                    print(len(fftAudio[0]))
                    plt.plot(fftAudio[0],fftAudio[1]) 
                    plt.title('Recebido', fontsize=18)
                    plt.xlabel('Frequencia (Hz)', fontsize=16)
                    plt.ylabel('Energia', fontsize=16)
                    plt.show()
                elif(ft == 'n'):
                    print('mostrar um zoom do grafico ? (Y ou N)')
                    zoom = input()
                    plt.plot(np.arange(len(audio) if zoom == 'n' else 1000),audio if zoom == 'n' else audio[40000:41000])
                    plt.show()
                else:
                    print('opcaoo invalida')
            elif(choice == '4'):
                print("\nModularizando com passa baixa")
                audio = self.LPF(audio,2000,self.fs)
                print('Modularizado!\nQuer reprouzir? (Y ou N)')
                choice = input()
                if(choice == 'y' or choice == 'Y'):
                    self.playSound(audio, wait = False)
                    print("Para parar aperte ENTER" )
                    input()
                    sd.stop()
            elif(choice == '5'):
                return
            else:
                print("\nalgo errado com a sua escolha\n")


            

nois = Noiszes()
while(True):
    nois.main()
