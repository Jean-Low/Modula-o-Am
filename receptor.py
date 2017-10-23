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
            self.ts = []
            self.stack = []
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
        xf = np.linspace(-1.0/(2.0*T), 1.0/(2.0*T), N)
        yf = fft(signal)
        return(xf, fftshift(yf))
    
    def FFT(self, audio):
        if(not isinstance(audio[0], float)):
            audio = audio[:,0]
        signal = fft(audio)
        
        if(audio.all() == signal.all()):
            print("\n\nO FFT N SERVE PARA NADA!!!!!!")
        signal = np.concatenate([signal[len(signal) / 2:],signal[0:len(signal) / 2]])
        XAxis = np.linspace(- self.fs / 2, self.fs / 2, len(signal))
        return (XAxis, signal);

    def gravar(self, tempo):
            audio = sd.rec(int(tempo*self.fs), self.fs, channels=1)
            sd.wait()
            self.wav = [audio,self.fs]
            maxAudio = max(audio)
            audio /= maxAudio
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
        

    def Somar(self, audio, audio2):
        listavazia= []
        if len(audio) > len(audio2):
            for v in range(len(audio)-len(audio2)):
                listavazia.append(0)
            audio2 = np.concatenate([audio2,listavazia])
            return audio + audio2
        elif len(audio2) > len(audio):
            for v in range(len(audio2)- len(audio)):
                listavazia.append(0)
            audio = np.concatenate([audio,listavazia])
            return audio + audio2
        else:
            return audio + audio2
    #isto transforma uma lista em .wav
    def escrever(self, nome_do_arquivo, som):
            sf.write('Saves/' + nome_do_arquivo + ".wav", som, self.fs)
            print("o destino foi escrito")     

    def desmodularizar(self, signal, freq):
                audio = signal
                if(not isinstance(signal[0], float)):
                    audio = signal[:,0]
                
                
                self.ts = np.linspace(0,len(audio) / self.fs,len(audio))
                
                fftAudio = self.FFT(np.sin(2*math.pi*freq*self.ts))
                plt.plot(fftAudio[0],fftAudio[1]) 
                plt.title('Recebido', fontsize=18)
                plt.xlabel('Frequencia (Hz)', fontsize=16)
                plt.ylabel('Energia', fontsize=16)
                plt.show()
            
                audio = audio*np.sin(2*math.pi*freq*self.ts)
                return audio
    
    def main(self):
        print('\nO que deseja fazer?\n1- Gravar um audio\n2- Carregar um audio')
        choice = input()
        if(choice == '1'):
            print('Vamos gravar um Audio!')
            print('Quantos segundos vamos gravar?')
            audio = self.gravar(int(input()))
            print('\nGravado!\nAgora o que deseja fazer?')
        elif(choice == '2'):
            print('Os seguintes arquivos foram encontrados:')
            fileList = []
            count = 0

            fileList2 = []
            count2 = 0

            for i in sorted(os.listdir('Saves')):

                print(str(count) + ' - ' + i)
                fileList.append(i)
                count+= 1

            while(True):
                print('Escolha o arquivo: (Sem o .wav)')
                choice = input()
                try:
                    if(choice.isdigit()):
                        print("\nLOADING BY INDEX")
                        self.wav, self.fs= sf.read("Saves/" + fileList[int(choice)]);
                        audio = self.wav
                        if(not isinstance(self.wav[0], float)):
                            audio = self.wav[:,0]
                    else:
                        print('\nLOADING BY NAME')
                        self.wav, self.fs = sf.read("Saves/" + choice + ".wav");
                        audio = self.wav
                        if(not isinstance(self.wav[0], float)):
                            audio = self.wav[:,0]

                    break
                except:
                    print('arquivo requisitado nao existe!!!\n')

        while(True):
            print('1- Salvar\n2- Reproduzir \n3- plotar grafico \n4- Aplicar passa baixa\n5- Tentar novamente\n6- Desmodularizar\n7- Adicionar na stack\n8- Reproduzir stack')
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
                    fftAudio = self.FFT(audio)
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
                print("\nDesmodularizar com passa baixa")
                print("\nFrequência de corte (deve ser igual à frequencia de corte na modularização)")
                while True:
                    try:
                        choice = int(input())
                        break
                    except:
                        print('Coloque uma frequencia valida')
                audio = self.LPF(audio,2000,self.fs)
                maxAudio = max(audio)
                print(maxAudio)
                audio /= maxAudio
                #self.stack.append([audio,choice]) #formato wavFreq
                
                print('Filtrado!\nQuer reprouzir? (Y ou N)')
                choice = input()
                if(choice == 'y' or choice == 'Y'):
                    self.playSound(audio, wait = False)
                    print("Para parar aperte ENTER" )
                    input()
                    sd.stop()
            elif(choice == '5'):
                return
            elif(choice == '6'):
                print('Frequência da desmodularização (deve ser igual à modularização):')
                while True:
                    try:
                        choice = int(input())
                        break
                    except:
                        print('Coloque uma frequencia valida')
                audio = self.desmodularizar(audio,choice)
                print("Desmodularizado")
            elif(choice == '7'):
                print('colocando na stack')
                self.stack.append(audio) #formato wavFreq
                print("salvo na stack na posição ", len(self.stack) - 1)
            elif(choice == '8'):
                print("Juntando canais...")
                stream = self.stack[0]
                
                for i in range(1,len(self.stack)):
                    stream = self.Somar(stream, self.stack[i]);
                    
                    fftAudio = self.FFT(stream)
                    plt.plot(fftAudio[0],fftAudio[1]) 
                    plt.title('Recebido', fontsize=18)
                    plt.xlabel('Frequencia (Hz)', fontsize=16)
                    plt.ylabel('Energia', fontsize=16)
                    plt.show()
                    
                print("Reproduzindo")
                self.playSound(audio, wait = False, looping = True)
                print("Para parar aperte ENTER" )
                input()
                sd.stop()
                
            else:
                print("\nalgo errado com a sua escolha\n")


nois = Noiszes()
while(True):
    nois.main()
