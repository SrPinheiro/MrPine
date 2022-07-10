import time
import threading
from pynput.mouse import Button, Controller as ControleMouse, Listener as MouseInfo
from pynput.keyboard import Listener as TecladoInfo, Key as chave,Controller as ControleTeclado
from plyer import notification

class inicio():
    try:
        forceBrute = True
        seguranca = True
        seguracaSoup = False
        ligado = False
        turbo = True
        direcao = True

        velocidadeMax = 0.05
        velocidade = 0.12
        sopa = 2
        sopaStatus = sopa

        mouse = ControleMouse()
        teclado = ControleTeclado()
        
        def clicar(self):
            try:
                while True:
                    if self.forceBrute:
                        if self.seguranca:
                            if self.ligado:
                                if self.direcao:
                                    self.mouse.click(Button.left)
                                else:
                                    self.mouse.click(Button.right)
                                if self.turbo:
                                    time.sleep(self.velocidadeMax)
                                else:
                                    time.sleep(self.velocidade)
            except:
                pass
        
        def Soup(self, Key):
            try:
                if Key == chave.end:
                    self.forceBrute = not self.forceBrute
                    notification.notify(
                            title = 'MrPine',
                            message = f'Mod: {"Ativado" if self.forceBrute else "Desativado"}',
                            timeout = 0.001,
                        )
                    
                if Key == chave.home:
                        self.seguracaSoup = not self.seguracaSoup
                        notification.notify(
                            title = 'MrPine',
                            message = f'Sopa: {"Ativado" if self.seguracaSoup else "Desativado"}\n{"mod: DESATIVADO" if not self.forceBrute else ""}',
                            timeout = 0.001,
                        )
                if self.forceBrute:
                    if self.seguracaSoup:
                        if f"{Key}"[1] == 'f' or f"{Key}"[1] == 'F':
                            if int(self.sopaStatus) < 9:
                                self.teclado.press(str(self.sopaStatus))
                                self.teclado.release(str(self.sopaStatus))
                                self.sopaStatus += 1
                                self.mouse.click(Button.right)
                                time.sleep(0.1)
                                self.teclado.press("q")
                                self.teclado.release("q")
                                self.teclado.press('1')
                                self.teclado.release('1')
                            
                            else:
                                self.sopaStatus = self.sopa
                                self.teclado.press(str(self.sopaStatus))
                                self.teclado.release(str(self.sopaStatus))
                                self.mouse.click(Button.right)
                                time.sleep(0.1)
                                self.teclado.press("q")
                                self.teclado.release("q")
                                self.teclado.press('1')
                                self.teclado.release('1')

                    
                        if f"{Key}"[1] == 'x' or f"{Key}"[1] == 'X':
                            self.teclado.press("e")
                            self.teclado.release("e")
                            time.sleep(0.01)

                            self.seguranca = False

                            with self.teclado.pressed(chave.shift):
                                self.mouse.position = (540, 30)
                                for i in range(0, (9 - self.sopa)):
                                    self.mouse.position = (540 + 35*i, 430)
                                    self.mouse.click(Button.right)
                                    time.sleep(0.01)

                            self.teclado.press("e")
                            self.teclado.release("e")

                            self.seguranca = True

                        if f"{Key}"[1] == 'z' or f"{Key}"[1] == 'Z':
                            self.teclado.press("e")
                            self.teclado.release("e")

                            self.seguranca = False

                            with self.teclado.pressed(chave.shift):
                                self.mouse.position = (540, 30)
                                for i in range(0,(9 - self.sopa)):
                                    self.mouse.position = (540 + 35*i, 465)
                                    self.mouse.click(Button.right)
                                    time.sleep(0.01)
                            self.teclado.press("e")
                            self.teclado.release("e")
                            
                            self.seguranca = True
                        
                        if f"{Key}"[1] == 'r' or f"{Key}"[1] == 'R':
                            pos_0 = (751,394)
                            pos_01 = (734,314)

                            pos_1 = (715,394)
                            pos_11 = (734,279)

                            pos_2 = (681,398)
                            pos_21 = (690,314)

                            pos_final = (807,295)

                            self.seguranca = False

                            self.teclado.press("e")
                            self.teclado.release("e")
                            time.sleep(0.1)

                            self.mouse.position = pos_2
                            self.mouse.click(Button.right)
                            self.mouse.position = pos_21
                            time.sleep(0.008)
                            self.mouse.click(Button.left)

                            self.mouse.position = pos_0
                            self.mouse.click(Button.right)
                            self.mouse.position = pos_01
                            time.sleep(0.008)
                            self.mouse.click(Button.left)

                            self.mouse.position = pos_1
                            self.mouse.click(Button.right)
                            self.mouse.position = pos_11
                            time.sleep(0.008)
                            self.mouse.click(Button.left)


                            time.sleep(0.1)
                            self.mouse.position = pos_final

                            with self.teclado.pressed(chave.shift):
                                self.mouse.click(Button.left)
                                time.sleep(0.08)


                            with self.teclado.pressed(chave.shift):
                                self.mouse.position = pos_01
                                self.mouse.click(Button.left)

                                self.mouse.position = pos_11
                                self.mouse.click(Button.left)

                                self.mouse.position = pos_21
                                self.mouse.click(Button.left)
                                time.sleep(0.1)

                            self.teclado.press("e")
                            self.teclado.release("e")

                            self.seguranca = True
            except:
                pass

        def UserClick(self, button, pressed):
            try:
                if pressed:
                    if button == Button.button8:
                        self.ligado = not self.ligado
                        notification.notify(
                            title = 'MrPine',
                            message = f'Clicker: {"Ativado" if self.ligado else "Desativado"}\n{"mod: DESATIVADO" if not self.forceBrute else ""}',
                            timeout = 0.001,
                        )

                    if button == Button.button9:
                        self.direcao = not self.direcao
                        notification.notify(
                            title = 'MrPine',
                            message = f'Estado: {"Ataque" if self.direcao else "Defesa"}\n{"mod: DESATIVADO" if not self.forceBrute else ""}',
                            timeout = 0.001,
                        )

                    if button == Button.middle:
                        self.turbo = not self.turbo
                        notification.notify(
                            title = 'MrPine',
                            message = f'Turbo: {"Ativado" if self.turbo else "Desativado"}\n{"mod: DESATIVADO" if not self.forceBrute else ""}',
                            timeout = 0.001,
                        )
            except:
                pass
    
        def AtualizarMouse(self):
            with MouseInfo(on_click = lambda a,b,c,d: self.UserClick( c, d,)) as mouse:
                mouse.join()

        def AtualizarTeclado(self): 
            with TecladoInfo(on_press = lambda a : self.Soup(a)) as teclado:
                teclado.join()

        def Iniciar(self):
            auto_click = threading.Thread(target = self.clicar).start()
            auto_mouse = threading.Thread(target = self.AtualizarMouse).start()
            auto_teclado = threading.Thread(target = self.AtualizarTeclado).start()

    except:
        print("Erro")

autoclick = inicio()
autoclick.Iniciar()


