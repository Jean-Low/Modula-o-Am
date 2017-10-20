import soundfile as sf
import sounddevice as sd



class Noiszes: 

        def __init__(self):

                self.fs = 44100

        def gravar(self, tempo):
                audio = sd.rec(int(tempo*self.fs), self.fs, channels=1)
                sd.wait()
                audio =audio[:,0]
                return audio




        #isto transforma uma lista em .wav
        def escrever(self, nome_do_arquivo, som):
                sf.write(nome_do_arquivo + ".wav", som, self.fs)
                print("o destino foi escrito")     



        def main(self):
                print('Aperta 1 pra continuar')
                numb = int(input())
                if(numb == 1):
                    print('Quantos seg')
                    audio = self.gravar(int(input()))      
                    print('Cabo de gravar, agr aperta 1 se for salvar ou qqr outra coisa se n for')
                    numb = int(input())
                    if(numb == 1):
                        print("Boa coroi, agr da nome pro arquivo")
                        name = input()
                        print("nice nome")
                        self.escrever(name, audio)
                    else:
                        print("fiquei titi")

                else:
                    print('Segue as instrução não seu merda')

nois = Noiszes()
nois.main()