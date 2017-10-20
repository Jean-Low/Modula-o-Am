import soundfile as sf
import sounddevice as sd
import os



class Noiszes: 

    def __init__(self):

            self.fs = 44100

    def playSound(self,sound,looping = False, wait = True):
            print("playing audio")
            sd.play(sound, self.fs,loop = looping)
            if(wait):
                sd.wait()

    def gravar(self, tempo):
            audio = sd.rec(int(tempo*self.fs), self.fs, channels=1)
            sd.wait()
            audio = audio[:,0]
            return audio

    #def Modular(self, audio):
            




    #isto transforma uma lista em .wav
    def escrever(self, nome_do_arquivo, som):
            sf.write('Saves/' + nome_do_arquivo + ".wav", som, self.fs)
            print("o destino foi escrito")     


    def main(self):
        print('\nO que deseja fazer?\n1- Gravar um audio\n2- Carregar um audio')
        choice = raw_input()
        print(choice)
        if(choice == '1'):
            print('Vamos gravar um Audio!')
            print('Quantos segundos vamos gravar?')
            audio = self.gravar(int(raw_input()))
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
                choice = raw_input()
                try:
                    try:
                        print("\nlOADING BY INDEX")
                        audio, self.fs = sf.read("Saves/" + fileList[int(choice)]);
                    except:
                        audio, self.fs = sf.read("Saves/" + choice + ".wav");
                    print('\nCarregado!\nAgora o que deseja fazer?')
                    break
                except:
                    print('arquivo requisitado nao existe!!!\n')
        else:
            print('Opa, algo esta errado com sua escolha!')
            return
        while(True):
            print('1- Savar\n2- Reproduzir')
            choice = raw_input()
            if(choice == '1'):
                print("Com qual nome devemos gravar")
                name = raw_input()
                self.escrever(name, audio)
                print("Salvo como: " + name )
            if(choice == '2'):
                print("Reproduzindo")
                self.playSound(audio, wait = False)
                print("Para parar aperte ENTER" )
                raw_input()
                sd.stop()
            else:
                print("\nalgo errado com a sua escolha\n")


            

nois = Noiszes()
while(True):
    nois.main()
