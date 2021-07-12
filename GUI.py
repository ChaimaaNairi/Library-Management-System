import tkinter as tk
from tkinter import messagebox
from tkinter.constants import END
from Business import Business
from LibraryData import *


class GUI:
    def __init__(self) -> None:
        self.business = Business()
        self.root = tk.Tk()
        self.root.configure(bg="darkseagreen")
        self.root.minsize(self.root.winfo_screenwidth() - 200, self.root.winfo_screenheight() - 200)
        self._currentFrames = []
        self._registerFrame: tk.Frame = None
        self._loginFrame: tk.Frame = None
        self._addBookFrame: tk.Frame = None
        self._editBookFrame: tk.Frame = None
        self._warningLabel: tk.Label = None
        self._customerFrames = {}
        self._adminFrames = {}

    ### HELPER FUNCTIONS ###

    def removeCurrentFrames(self):
        for frame in self._currentFrames:
            frame.place_forget()
        self._currentFrames = []
        self._warningLabel = None

    def placeFrameCenter(self, frame: tk.Frame, pixelh: int, pixelw: int) -> None:
        wih = self.root.winfo_height()
        wiw = self.root.winfo_width()
        sch = self.root.winfo_screenheight()
        scw = self.root.winfo_screenwidth()
        if (wih == 1):
            wih = sch - 100
            wiw = scw - 100
        adjrely = (wih - pixelh) / (2 * wih)
        adjrelx = (wiw - pixelw) / (2 * wiw)
        frame.place(relx=adjrelx, rely=adjrely, height=pixelh, width=pixelw)

    def placeFrames111Formation(self, frameL: tk.Frame, frameC: tk.Frame, frameR: tk.Frame):
        edgeOffset = 0.005
        frameL.place(rely=0 + 2 * edgeOffset, relx=0 + edgeOffset, relheight=1 - 4 * edgeOffset,
                     relwidth=0.2 - edgeOffset)
        frameC.place(rely=0 + 2 * edgeOffset, relx=0.2 + edgeOffset, relheight=1 - 4 * edgeOffset,
                     relwidth=0.4 - edgeOffset)
        frameR.place(rely=0 + 2 * edgeOffset, relx=0.6 + edgeOffset, relheight=1 - 4 * edgeOffset,
                     relwidth=0.4 - 2 * edgeOffset)

    def placeFrames13Formation(self, frame1: tk.Frame, frame2: tk.Frame, frame3: tk.Frame, frame4: tk.Frame):
        edgeOffset = 0.005
        frame1.place(rely=0 + edgeOffset, relx=0 + edgeOffset, relheight=1 - 2 * edgeOffset,
                     relwidth=0.175 - edgeOffset)
        frame2.place(rely=0 + edgeOffset, relx=0.175 + edgeOffset, relheight=1 - 2 * edgeOffset,
                     relwidth=0.275 - edgeOffset)
        frame3.place(rely=0 + edgeOffset, relx=0.45 + edgeOffset, relheight=1 - 2 * edgeOffset,
                     relwidth=0.275 - edgeOffset)
        frame4.place(rely=0 + edgeOffset, relx=0.725 + edgeOffset, relheight=1 - 2 * edgeOffset,
                     relwidth=0.275 - 2 * edgeOffset)

    def setWarningLabel(self, message: str):
        if self._warningLabel != None:
            self._warningLabel.configure(text=message)
            return
        self.warningPopup(message)

    def warningPopup(self, message):
        messagebox.showwarning("Warning", message)

    ### FRAMES ###

    def showRegisterFrame(self):
        pixelh = 310
        pixelw = 260
        if (self._registerFrame != None):
            self.removeCurrentFrames()
            self.placeFrameCenter(self._registerFrame, pixelh, pixelw)
            self._currentFrames += [self._registerFrame]
            return
        self.removeCurrentFrames()
        self._registerFrame = registerFrame = tk.Frame(self.root)
        self._currentFrames += [self._registerFrame]
        self.placeFrameCenter(self._registerFrame, pixelh, pixelw)
        self.RFlabelUsername = tk.Label(self._registerFrame)
        self.RFlabelUsername.configure(anchor='e', compound='top', text='Kullanıcı Adı:',font='{Arial TUR} 8 {bold}')
        self.RFlabelUsername.place(anchor='nw', relheight='0.1', relwidth='0.28', relx='0.03', rely='0.1', x='0', y='0')
        self.RFlabelPassword = tk.Label(self._registerFrame)
        self.RFlabelPassword.configure(anchor='e', text='Şifre:',font='{Arial TUR} 8 {bold}')
        self.RFlabelPassword.place(anchor='nw', relheight='0.1', relwidth='0.28', relx='0.03', rely='0.3', x='0', y='0')
        self.RFentryUsername = tk.Entry(self._registerFrame)
        self.RFentryUsername.place(anchor='nw', relheight='0.1', relwidth='0.55', relx='0.35', rely='0.1', x='0', y='0')
        self.RFentryPassword = tk.Entry(self._registerFrame)
        self.RFentryPassword.configure(show='•')
        self.RFentryPassword.place(anchor='nw', relheight='0.1', relwidth='0.55', relx='0.35', rely='0.3', x='0', y='0')
        self.RFlabelWarning = tk.Label(self._registerFrame)
        self.RFlabelWarning.configure(anchor='center', foreground='#ff0000', text='')
        self.RFlabelWarning.place(anchor='nw', relheight='0.1', relwidth='0.9', relx='0.05', rely='0.68', x='0', y='0')
        self.RFcheckVar = tk.IntVar()
        self.RFcheckAdmin = tk.Checkbutton(self._registerFrame, variable=self.RFcheckVar)
        self.RFcheckAdmin.configure(anchor='w', text='Yönetici',bg='rosybrown')
        self.RFcheckAdmin.place(anchor='nw', relheight='.1', relwidth='0.35', relx='.1', rely='.5', x='0', y='0')
        self.RFbuttonRegister = tk.Button(self._registerFrame)
        self.RFbuttonRegister.configure(text='Kaydol',bg='grey', command=self.buttonRegisterAction)
        self.RFbuttonRegister.place(anchor='nw', relx='0.68', rely='0.82', x='0', y='0')
        self.RFbuttonHaveAcc = tk.Button(self._registerFrame, command=self.buttonHaveAccAction)
        self.RFbuttonHaveAcc.configure(text='Hesabım Var',bg='grey')
        self.RFbuttonHaveAcc.place(anchor='nw', relx='0.1', rely='0.82', x='0', y='0')
        self._warningLabel = self.RFlabelWarning
        return registerFrame

    def showLoginFrame(self):
        pixelh = 310
        pixelw = 260
        if (self._loginFrame != None):
            self.removeCurrentFrames()
            self.placeFrameCenter(self._loginFrame, pixelh, pixelw)
            self._currentFrames += [self._loginFrame]
            return
        self.removeCurrentFrames()
        self._loginFrame = loginFrame = tk.Frame(self.root)
        self._currentFrames += [self._loginFrame]
        self.placeFrameCenter(self._loginFrame, pixelh, pixelw)
        self.LFlabelUsername = tk.Label(self._loginFrame)
        self.LFlabelUsername.configure(anchor='e', compound='top', text='Kullanıcı Adı:',font='{Arial TUR} 8 {bold}')
        self.LFlabelUsername.place(anchor='nw', relheight='0.1', relwidth='0.28', relx='0.03', rely='0.1', x='0', y='0')
        self.LFlabelPassword = tk.Label(self._loginFrame)
        self.LFlabelPassword.configure(anchor='e', text='Şifre:',font='{Arial TUR} 8 {bold}')
        self.LFlabelPassword.place(anchor='nw', relheight='0.1', relwidth='0.28', relx='0.03', rely='0.3', x='0', y='0')
        self.LFentryUsername = tk.Entry(self._loginFrame)
        self.LFentryUsername.place(anchor='nw', relheight='0.1', relwidth='0.55', relx='0.35', rely='0.1', x='0', y='0')
        self.LFentryPassword = tk.Entry(self._loginFrame)
        self.LFentryPassword.configure(show='•')
        self.LFentryPassword.place(anchor='nw', relheight='0.1', relwidth='0.55', relx='0.35', rely='0.3', x='0', y='0')
        self.LFlabelWarning = tk.Label(self._loginFrame)
        self.LFlabelWarning.configure(anchor='center', foreground='#ff0000', text='')
        self.LFlabelWarning.place(anchor='nw', relheight='0.1', relwidth='0.9', relx='0.05', rely='0.58', x='0', y='0')
        self.LFbuttonLogin = tk.Button(self._loginFrame, command=self.buttonLoginAction)
        self.LFbuttonLogin.configure(text='Giriş Yap',bg='grey')
        self.LFbuttonLogin.place(anchor='nw', relx='0.68', rely='0.82', x='0', y='0')
        self.LFbuttonNoAcc = tk.Button(self._loginFrame, command=self.buttonNoAccAction)
        self.LFbuttonNoAcc.configure(text='Hesabım Yok',bg='grey')
        self.LFbuttonNoAcc.place(anchor='nw', relx='0.1', rely='0.82', x='0', y='0')
        self._warningLabel = self.LFlabelWarning
        return loginFrame

    def showCustomerViewFrames(self):
        self.removeCurrentFrames()
        ### info frame
        if "libinfo" not in self._customerFrames:
            self._customerFrames["libinfo"] = infoFrame = tk.Frame(self.root)
            self.CIFusernameVarLabel = tk.Label(infoFrame)
            self.CIFusernameVarLabel.configure(text='label username')
            self.CIFusernameVarLabel.place(anchor='nw', relheight='0.05', relwidth='0.52', relx='0.05', rely='0.03',
                                           x='0', y='0')
            self.CIFlogoutButton = tk.Button(infoFrame, command=self.logoutButtonAction)
            self.CIFlogoutButton.configure(text='Çıkış Yap',bg='grey')
            self.CIFlogoutButton.place(anchor='nw', relheight='0.05', relx='0.62', rely='0.03', x='0', y='0')
            self.CIFinfoConstLabel = tk.Label(infoFrame)
            self.CIFinfoConstLabel.configure(font='{Arial TUR} 12 {}', text='Kütüphane Bilgileri',bg='rosybrown')
            self.CIFinfoConstLabel.place(anchor='nw', relwidth='1.0', relx='0.0', rely='0.48', x='0', y='0')
            self.CIFcustomerCountConstLabel = tk.Label(infoFrame)
            self.CIFcustomerCountConstLabel.configure(font='{Arial TUR} 9 {bold}',anchor='w', text='Kullanıcı Sayısı:')
            self.CIFcustomerCountConstLabel.place(anchor='nw', relheight='0.05', relwidth='0.6', relx='0.1',
                                                  rely='0.65', x='0', y='0')
            self.CIFcustomerCountVarLabel = tk.Label(infoFrame)
            self.CIFcustomerCountVarLabel.configure(anchor='w', text='0')
            self.CIFcustomerCountVarLabel.place(anchor='nw', relheight='0.05', relwidth='0.2', relx='0.75', rely='0.65',
                                                x='0', y='0')
            self.CIFbookCountConstLabel = tk.Label(infoFrame)
            self.CIFbookCountConstLabel.configure(font='{Arial TUR} 9 {bold}',anchor='w', text='Kitap Sayısı:')
            self.CIFbookCountConstLabel.place(anchor='nw', relheight='0.05', relwidth='0.6', relx='0.1', rely='0.75',
                                              x='0', y='0')
            self.CIFbookCountVarLabel = tk.Label(infoFrame)
            self.CIFbookCountVarLabel.configure(anchor='w', text='0')
            self.CIFbookCountVarLabel.place(anchor='nw', relheight='0.05', relwidth='0.2', relx='0.75', rely='0.75',
                                            x='0', y='0')
            self.CIFlabel3 = tk.Label(infoFrame)
            self.CIFlabel3.configure(font='{Arial TUR} 12 {}', text='Kullanıcı Bilgileri',bg='rosybrown')
            self.CIFlabel3.place(anchor='nw', relwidth='1.0', relx='0.0', rely='0.1', x='0', y='0')
            self.CIFuserTypeConstLabel = tk.Label(infoFrame)
            self.CIFuserTypeConstLabel.configure(font='{Arial TUR} 9 {bold}',anchor='w', text='Kullanıcı Tipi:')
            self.CIFuserTypeConstLabel.place(anchor='nw', relheight='0.05', relwidth='0.4', relx='0.1', rely='0.17',
                                             x='0', y='0')
            self.CIFuserTypeVarLabel = tk.Label(infoFrame)
            self.CIFuserTypeVarLabel.configure(anchor='w', text='Müşteri')
            self.CIFuserTypeVarLabel.place(anchor='nw', relheight='0.05', relwidth='0.4', relx='0.55', rely='0.17',
                                           x='0', y='0')
            self.CIFusernamePanelConstLabel = tk.Label(infoFrame)
            self.CIFusernamePanelConstLabel.configure(font='{Arial TUR} 9 {bold}',anchor='w', text='Kullanıcı Adı:')
            self.CIFusernamePanelConstLabel.place(anchor='nw', relheight='0.05', relwidth='0.4', relx='0.1',
                                                  rely='0.27', x='0', y='0')
            self.CIFusernamePanelVarLabel = tk.Label(infoFrame)
            self.CIFusernamePanelVarLabel.configure(anchor='w', text='0')
            self.CIFusernamePanelVarLabel.place(anchor='nw', relheight='0.05', relwidth='0.4', relx='0.55', rely='0.27',
                                                x='0', y='0')
            self.CIFborrowedBookCountConstLable = tk.Label(infoFrame)
            self.CIFborrowedBookCountConstLable.configure(font='{Arial TUR} 9 {bold}',anchor='w', text='Ödünç Alınan Kitap:')
            self.CIFborrowedBookCountConstLable.place(anchor='nw', relheight='0.05', relwidth='0.6', relx='0.1',
                                                      rely='0.37', x='0', y='0')
            self.CIFborrowedBookCountVarLabel = tk.Label(infoFrame)
            self.CIFborrowedBookCountVarLabel.configure(anchor='w', text='0')
            self.CIFborrowedBookCountVarLabel.place(anchor='nw', relheight='0.05', relwidth='0.2', relx='0.75',
                                                    rely='0.37', x='0', y='0')

        ### Frame showing library books to customer
        if "library" not in self._customerFrames:
            self._customerFrames["library"] = libraryFrame = tk.Frame(self.root)
            self.CLFlabel1 = tk.Label(libraryFrame)
            self.CLFlabel1.configure(font='{Arial TUR} 12 {bold}', text='Kütüphanede Mevcut Olan Kitaplar',bg='darkseagreen')
            self.CLFlabel1.place(anchor='nw', relheight='0.07', relwidth='1.0', relx='0.0', x='0', y='0')
            self.CLFlistbox1 = tk.Listbox(libraryFrame)
            self.CLFlistbox1.bind("<<ListboxSelect>>", self.customerLibraryBookListSelect)
            self.CLFlistbox1.place(anchor='nw', relheight='0.51', relwidth='1.0', relx='0.0', rely='0.09', x='0', y='0')
            self.CLFlabel2 = tk.Label(libraryFrame)
            self.CLFlabel2.configure(font='{Arial TUR} 13 {}', text='Seçilmiş Kitabın Detayları',bg='lightgrey')
            self.CLFlabel2.place(anchor='nw', relheight='0.05', relwidth='1.0', relx='0.0', rely='0.62', x='0', y='0')
            self.CLFtitleConstLabel = tk.Label(libraryFrame)
            self.CLFtitleConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.CLFtitleConstLabel.configure(font='{Arial TUR} 11 {bold}',text='Başlık:')
            self.CLFtitleConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.05', rely='0.7', x='0',
                                          y='0')
            self.CLFtitleVarLabel = tk.Label(libraryFrame)
            self.CLFtitleVarLabel.configure(anchor='w', cursor='based_arrow_down', font='{Arial TUR} 12 {}',
                                            justify='left')
            self.CLFtitleVarLabel.configure(takefocus=False, text='')
            self.CLFtitleVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.67', relx='0.28', rely='0.7', x='0',
                                        y='0')
            self.CLFauthorConstLabel = tk.Label(libraryFrame)
            self.CLFauthorConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.CLFauthorConstLabel.configure(font='{Arial TUR} 11 {bold}',text='Yazar:')
            self.CLFauthorConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.05', rely='0.75',
                                           x='0', y='0')
            self.CLFauthorVarLabel = tk.Label(libraryFrame)
            self.CLFauthorVarLabel.configure(anchor='w', cursor='based_arrow_down', font='{Arial TUR} 12 {}',
                                             justify='left')
            self.CLFauthorVarLabel.configure(takefocus=False, text='')
            self.CLFauthorVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.67', relx='0.28', rely='0.75',
                                         x='0', y='0')
            self.CLFborrowButton = tk.Button(libraryFrame, command=self.borrowBookButtonAction)
            self.CLFborrowButton.configure(text='Kitabı Ödünç Al',bg='grey')
            self.CLFborrowButton.place(anchor='nw', relx='0.6', rely='0.9', x='0', y='0')
            self.CLFidConstLabel = tk.Label(libraryFrame)
            self.CLFidConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.CLFidConstLabel.configure(font='{Arial TUR} 11 {bold}',text='ID:')
            self.CLFidConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.05', rely='0.82', x='0',
                                       y='0')
            self.CLFidVarLabel = tk.Label(libraryFrame)
            self.CLFidVarLabel.configure(anchor='w', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.CLFidVarLabel.configure(text='')
            self.CLFidVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.25', rely='0.82', x='0',
                                     y='0')
            self.CLFpriceConstLabel = tk.Label(libraryFrame)
            self.CLFpriceConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.CLFpriceConstLabel.configure(font='{Arial TUR} 11 {bold}',text='Fiyat:')
            self.CLFpriceConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.45', rely='0.82',
                                          x='0', y='0')
            self.CLFpriceVarLabel = tk.Label(libraryFrame)
            self.CLFpriceVarLabel.configure(anchor='w', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.CLFpriceVarLabel.configure(text='')
            self.CLFpriceVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.65', rely='0.82', x='0',
                                        y='0')
            self.CLFstockConstLabel = tk.Label(libraryFrame)
            self.CLFstockConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.CLFstockConstLabel.configure(font='{Arial TUR} 11 {bold}',text='Stok:')
            self.CLFstockConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.05', rely='0.9', x='0',
                                          y='0')
            self.CLFstockVarLabel = tk.Label(libraryFrame)
            self.CLFstockVarLabel.configure(anchor='w', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.CLFstockVarLabel.configure(text='')
            self.CLFstockVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.25', rely='0.9', x='0',
                                        y='0')

        ###
        if "borrowed" not in self._customerFrames:
            self._customerFrames["borrowed"] = borrowedFrame = tk.Frame(self.root)
            self.CBFlabel1 = tk.Label(borrowedFrame)
            self.CBFlabel1.configure(font='{Arial TUR} 12 {bold}', text='Sizin Ödünç Aldığınız Kitaplar',bg='darkseagreen')
            self.CBFlabel1.place(anchor='nw', relheight='0.07', relwidth='1.0', relx='0.0', x='0', y='0')
            self.CBFlistbox1 = tk.Listbox(borrowedFrame)
            self.CBFlistbox1.bind("<<ListboxSelect>>", self.customerBorrowedBookListSelect)
            self.CBFlistbox1.place(anchor='nw', relheight='0.51', relwidth='1.0', relx='0.0', rely='0.09', x='0', y='0')
            self.CBFlabel2 = tk.Label(borrowedFrame)
            self.CBFlabel2.configure(font='{Arial TUR} 13 {}', text='Seçilmiş Kitabın Detayları',bg='lightgrey')
            self.CBFlabel2.place(anchor='nw', relheight='0.05', relwidth='1.0', relx='0.0', rely='0.62', x='0', y='0')
            self.CBFtitleConstLabel = tk.Label(borrowedFrame)
            self.CBFtitleConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.CBFtitleConstLabel.configure(font='{Arial TUR} 11 {bold}',text='Başlık:')
            self.CBFtitleConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.05', rely='0.7', x='0',
                                          y='0')
            self.CBFtitleVarLabel = tk.Label(borrowedFrame)
            self.CBFtitleVarLabel.configure(anchor='w', cursor='based_arrow_down', font='{Arial TUR} 12 {}',
                                            justify='left')
            self.CBFtitleVarLabel.configure(takefocus=False, text='')
            self.CBFtitleVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.67', relx='0.28', rely='0.7', x='0',
                                        y='0')
            self.CBFauthorConstLabel = tk.Label(borrowedFrame)
            self.CBFauthorConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.CBFauthorConstLabel.configure(font='{Arial TUR} 11 {bold}',text='Yazar:')
            self.CBFauthorConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.05', rely='0.75',
                                           x='0', y='0')
            self.CBFauthorVarLabel = tk.Label(borrowedFrame)
            self.CBFauthorVarLabel.configure(anchor='w', cursor='based_arrow_down', font='{Arial TUR} 12 {}',
                                             justify='left')
            self.CBFauthorVarLabel.configure(takefocus=False, text='')
            self.CBFauthorVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.67', relx='0.28', rely='0.75',
                                         x='0', y='0')
            self.CBFborrowButton = tk.Button(borrowedFrame, command=self.returnBookButtonAction)
            self.CBFborrowButton.configure(text='Kitabı İade Et',bg='grey')
            self.CBFborrowButton.place(anchor='nw', relx='0.6', rely='0.9', x='0', y='0')
            self.CBFidConstLabel = tk.Label(borrowedFrame)
            self.CBFidConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.CBFidConstLabel.configure(font='{Arial TUR} 11 {bold}',text='ID:')
            self.CBFidConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.05', rely='0.82', x='0',
                                       y='0')
            self.CBFidVarLabel = tk.Label(borrowedFrame)
            self.CBFidVarLabel.configure(anchor='w', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.CBFidVarLabel.configure(text='')
            self.CBFidVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.25', rely='0.82', x='0',
                                     y='0')
            self.CBFpriceConstLabel = tk.Label(borrowedFrame)
            self.CBFpriceConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.CBFpriceConstLabel.configure(font='{Arial TUR} 11 {bold}',text='Fiyat:')
            self.CBFpriceConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.45', rely='0.82',
                                          x='0', y='0')
            self.CBFriceVarLabel = tk.Label(borrowedFrame)
            self.CBFriceVarLabel.configure(anchor='w', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.CBFriceVarLabel.configure(text='')
            self.CBFriceVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.65', rely='0.82', x='0',
                                       y='0')
            self.CBFstockConstLabel = tk.Label(borrowedFrame)
            self.CBFstockConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.CBFstockConstLabel.configure(font='{Arial TUR} 11 {bold}',text='Stok:')
            self.CBFstockConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.05', rely='0.9', x='0',
                                          y='0')
            self.CBFstockVarLabel = tk.Label(borrowedFrame)
            self.CBFstockVarLabel.configure(anchor='w', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.CBFstockVarLabel.configure(text='')
            self.CBFstockVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.25', rely='0.9', x='0',
                                        y='0')
        self._currentFrames += [self._customerFrames["libinfo"], self._customerFrames["library"],
                                self._customerFrames["borrowed"]]
        self.placeFrames111Formation(self._customerFrames["libinfo"], self._customerFrames["library"],
                                     self._customerFrames["borrowed"])
        self.updateCustomerInfoFrame()
        self.updateCustomerBorrowedBookList()
        self.updateCustomerLibraryBookList()

    def showAdminViewFrames(self):
        self.removeCurrentFrames()
        if "info" not in self._adminFrames:
            self._adminFrames["info"] = infoframe = tk.Frame(self.root)
            self.AIFusernameVarLabel = tk.Label(infoframe)
            self.AIFusernameVarLabel.configure(text='label32')
            self.AIFusernameVarLabel.place(anchor='nw', relheight='0.05', relwidth='0.52', relx='0.05', rely='0.03',
                                           x='0', y='0')
            self.AIFlogoutButton = tk.Button(infoframe)
            self.AIFlogoutButton.configure(text='Çıkış Yap', command=self.logoutButtonAction, bg='darkgrey')
            self.AIFlogoutButton.place(anchor='nw', relheight='0.05', relx='0.62', rely='0.03', x='0', y='0')
            self.AIFinfoConstLabel = tk.Label(infoframe)
            self.AIFinfoConstLabel.configure(font='{Arial TUR} 12 {}', text='Kütüphane Bilgileri',bg='rosybrown')
            self.AIFinfoConstLabel.place(anchor='nw', relwidth='1.0', relx='0.0', rely='0.48', x='0', y='0')
            self.AIFcustomerCountConstLabel = tk.Label(infoframe)
            self.AIFcustomerCountConstLabel.configure(font='{Arial TUR} 9 {bold}',anchor='w', text='Kullanıcı Sayısı:')
            self.AIFcustomerCountConstLabel.place(anchor='nw', relheight='0.05', relwidth='0.6', relx='0.1',
                                                  rely='0.65', x='0', y='0')
            self.AIFcustomerCountVarLabel = tk.Label(infoframe)
            self.AIFcustomerCountVarLabel.configure(anchor='w', text='0')
            self.AIFcustomerCountVarLabel.place(anchor='nw', relheight='0.05', relwidth='0.2', relx='0.75', rely='0.65',
                                                x='0', y='0')
            self.AIFbookCountConstLabel = tk.Label(infoframe)
            self.AIFbookCountConstLabel.configure(font='{Arial TUR} 9 {bold}',anchor='w', text='Kitap Sayısı:')
            self.AIFbookCountConstLabel.place(anchor='nw', relheight='0.05', relwidth='0.6', relx='0.1', rely='0.75',
                                              x='0', y='0')
            self.AIFbookCountVarLabel = tk.Label(infoframe)
            self.AIFbookCountVarLabel.configure(anchor='w', text='0')
            self.AIFbookCountVarLabel.place(anchor='nw', relheight='0.05', relwidth='0.2', relx='0.75', rely='0.75',
                                            x='0', y='0')
            self.AIFlabel3 = tk.Label(infoframe)
            self.AIFlabel3.configure(font='{Arial TUR} 12 {}', text='Kullanıcı Bilgileri',bg='rosybrown')
            self.AIFlabel3.place(anchor='nw', relwidth='1.0', relx='0.0', rely='0.1', x='0', y='0')
            self.AIFuserTypeConstLabel = tk.Label(infoframe)
            self.AIFuserTypeConstLabel.configure(font='{Arial TUR} 9 {bold}',anchor='w', text='Kullanıcı Tipi:')
            self.AIFuserTypeConstLabel.place(anchor='nw', relheight='0.05', relwidth='0.4', relx='0.1', rely='0.17',
                                             x='0', y='0')
            self.AIFuserTypeVarLabel = tk.Label(infoframe)
            self.AIFuserTypeVarLabel.configure(anchor='w', text='0')
            self.AIFuserTypeVarLabel.place(anchor='nw', relheight='0.05', relwidth='0.4', relx='0.55', rely='0.17',
                                           x='0', y='0')
            self.AIFusernamePanelConstLabel = tk.Label(infoframe)
            self.AIFusernamePanelConstLabel.configure(font='{Arial TUR} 9 {bold}',anchor='w', text='Kullanıcı Adı:')
            self.AIFusernamePanelConstLabel.place(anchor='nw', relheight='0.05', relwidth='0.4', relx='0.1',
                                                  rely='0.27', x='0', y='0')
            self.AIFusernamePanelVarLabel = tk.Label(infoframe)
            self.AIFusernamePanelVarLabel.configure(anchor='w', text='0')
            self.AIFusernamePanelVarLabel.place(anchor='nw', relheight='0.05', relwidth='0.4', relx='0.55', rely='0.27',
                                                x='0', y='0')
        if "users" not in self._adminFrames:
            self._adminFrames["users"] = libraryUsers = tk.Frame(self.root)
            self.AULlabel1 = tk.Label(libraryUsers)
            self.AULlabel1.configure(font='{Arial TUR} 12 {bold}', text='Kütüphanede Mevcut Olan Kullancılar',bg='darkseagreen')
            self.AULlabel1.place(anchor='nw', relheight='0.07', relwidth='1.0', relx='0.0', x='0', y='0')
            self.AULusersListbox = tk.Listbox(libraryUsers)
            self.AULusersListbox.bind("<<ListboxSelect>>", self.adminUserListSelect)
            self.AULusersListbox.place(anchor='nw', relheight='0.54', relwidth='1.0', relx='0.0', rely='0.09', x='0',
                                       y='0')
            self.AULlabel2 = tk.Label(libraryUsers)
            self.AULlabel2.configure(font='{Arial TUR} 13 {}', text='Seçilmiş Kullancının Detayları',bg='lightgrey')
            self.AULlabel2.place(anchor='nw', relheight='0.1', relwidth='1.0', relx='0.0', rely='0.62', x='0', y='0')
            self.AULusernameConstLabel = tk.Label(libraryUsers)
            self.AULusernameConstLabel.configure(anchor='w', font='{Arial TUR} 11 {bold}', text='Kullacnı Adı:')
            self.AULusernameConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.3', relx='0.05', rely='0.72',
                                             x='0', y='0')
            self.AULusernameVarLabel = tk.Label(libraryUsers)
            self.AULusernameVarLabel.configure(anchor='w', cursor='based_arrow_down', font='{Arial TUR} 12 {}',
                                               justify='left')
            self.AULusernameVarLabel.configure(takefocus=False, text='')
            self.AULusernameVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.67', relx='0.37', rely='0.72',
                                           x='0', y='0')
            self.AULusertypeConstLabel = tk.Label(libraryUsers)
            self.AULusertypeConstLabel.configure(anchor='w', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.AULusertypeConstLabel.configure(font='{Arial TUR} 11 {bold}',text='Kullancı Tipi:')
            self.AULusertypeConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.3', relx='0.05', rely='0.77',
                                             x='0', y='0')
            self.AULtypeVarLabel = tk.Label(libraryUsers)
            self.AULtypeVarLabel.configure(anchor='w', cursor='based_arrow_down', font='{Arial TUR} 12 {}',
                                           justify='left')
            self.AULtypeVarLabel.configure(takefocus=False, text='')
            self.AULtypeVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.67', relx='0.37', rely='0.77', x='0',
                                       y='0')
            self.AULidConstLabel = tk.Label(libraryUsers)
            self.AULidConstLabel.configure(anchor='w', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.AULidConstLabel.configure(font='{Arial TUR} 11 {bold}',text='ID:')
            self.AULidConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.1', relx='0.05', rely='0.82', x='0',
                                       y='0')
            self.AULidVarLabel = tk.Label(libraryUsers)
            self.AULidVarLabel.configure(anchor='w', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.AULidVarLabel.configure(text='')
            self.AULidVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.1', relx='0.2', rely='0.82', x='0',
                                     y='0')
            self.AULborrowedBooksConstLabel = tk.Label(libraryUsers)
            self.AULborrowedBooksConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}',
                                                      justify='left')
            self.AULborrowedBooksConstLabel.configure(font='{Arial TUR} 12 {bold}',text='Aldığı Kitaplar:')
            self.AULborrowedBooksConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.47', relx='0.35',
                                                  rely='0.82', x='0', y='0')
            self.AULborrowedBooksVarLabel = tk.Label(libraryUsers)
            self.AULborrowedBooksVarLabel.configure(anchor='w', cursor='arrow', font='{Arial TUR} 12 {}',
                                                    justify='left')
            self.AULborrowedBooksVarLabel.configure(text='')
            self.AULborrowedBooksVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.82', rely='0.82',
                                                x='0', y='0')
        if "userbooks" not in self._adminFrames:
            self._adminFrames["userbooks"] = userBooks = tk.Frame(self.root)
            self.AUBlabel1 = tk.Label(userBooks)
            self.AUBlabel1.configure(font='{Arial TUR} 12 {bold}', text='Müşterinin Ödünç Aldığı Kitaplar',bg='darkseagreen')
            self.AUBlabel1.place(anchor='nw', relheight='0.07', relwidth='1.0', relx='0.0', x='0', y='0')
            self.AUBbooksListbox = tk.Listbox(userBooks)
            self.AUBbooksListbox.bind("<<ListboxSelect>>", self.adminBorrowedBookListSelect)
            self.AUBbooksListbox.place(anchor='nw', relheight='0.41', relwidth='1.0', relx='0.0', rely='0.09', x='0',
                                       y='0')
            self.AUBlabel2 = tk.Label(userBooks)
            self.AUBlabel2.configure(font='{Arial TUR} 13 {}', text='Seçilmiş Kitabın Detayları',bg='lightgrey')
            self.AUBlabel2.place(anchor='nw', relheight='0.05', relwidth='1.0', relx='0.0', rely='0.52', x='0', y='0')
            self.AUBtitleConstLabel = tk.Label(userBooks)
            self.AUBtitleConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.AUBtitleConstLabel.configure(font='{Arial TUR} 11 {bold}',text='Başlık:')
            self.AUBtitleConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.05', rely='0.6', x='0',
                                          y='0')
            self.AUBtitleVarLabel = tk.Label(userBooks)
            self.AUBtitleVarLabel.configure(anchor='w', cursor='based_arrow_down', font='{Arial TUR} 12 {}',
                                            justify='left')
            self.AUBtitleVarLabel.configure(takefocus=False, text='')
            self.AUBtitleVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.67', relx='0.28', rely='0.6', x='0',
                                        y='0')
            self.AUBauthorConstLabel = tk.Label(userBooks)
            self.AUBauthorConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.AUBauthorConstLabel.configure(font='{Arial TUR} 11 {bold}',text='Yazar:')
            self.AUBauthorConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.05', rely='0.67',
                                           x='0', y='0')
            self.AUBauthorVarLabel = tk.Label(userBooks)
            self.AUBauthorVarLabel.configure(anchor='w', cursor='based_arrow_down', font='{Arial TUR} 12 {}',
                                             justify='left')
            self.AUBauthorVarLabel.configure(takefocus=False, text='')
            self.AUBauthorVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.67', relx='0.28', rely='0.67',
                                         x='0', y='0')
            self.AUBtakeBookButton = tk.Button(userBooks)
            self.AUBtakeBookButton.configure(text='Kitabı Geri Al', command=self.adminReturnBookButtonAction,bg='grey')
            self.AUBtakeBookButton.place(anchor='nw', relwidth='0.3', relx='0.6', rely='0.9', x='0', y='0')
            self.AUBidConstLabel = tk.Label(userBooks)
            self.AUBidConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.AUBidConstLabel.configure(font='{Arial TUR} 12 {bold}',text='ID:')
            self.AUBidConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.05', rely='0.74', x='0',
                                       y='0')
            self.AUBidVarLabel = tk.Label(userBooks)
            self.AUBidVarLabel.configure(anchor='w', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.AUBidVarLabel.configure(text='')
            self.AUBidVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.25', rely='0.74', x='0',
                                     y='0')
            self.AUBpriceConstLabel = tk.Label(userBooks)
            self.AUBpriceConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.AUBpriceConstLabel.configure(font='{Arial TUR} 11 {bold}',text='Fiyat:')
            self.AUBpriceConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.45', rely='0.75',
                                          x='0', y='0')
            self.AUBpriceVarLabel = tk.Label(userBooks)
            self.AUBpriceVarLabel.configure(anchor='w', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.AUBpriceVarLabel.configure(text='')
            self.AUBpriceVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.65', rely='0.75', x='0',
                                        y='0')
            self.AUBstockConstLabel = tk.Label(userBooks)
            self.AUBstockConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.AUBstockConstLabel.configure(font='{Arial TUR} 11 {bold}',text='Stok:')
            self.AUBstockConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.05', rely='0.82',
                                          x='0', y='0')
            self.AUBstockVarLabel = tk.Label(userBooks)
            self.AUBstockVarLabel.configure(anchor='w', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.AUBstockVarLabel.configure(text='')
            self.AUBstockVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.25', rely='0.82', x='0',
                                        y='0')
        if "libbooks" not in self._adminFrames:
            self._adminFrames["libbooks"] = libraryBooks = tk.Frame(self.root)
            self.ALBlabel1 = tk.Label(libraryBooks)
            self.ALBlabel1.configure(font='{Arial TUR} 12 {bold}', text='Kütüphanede Mevcut Olan Kitaplar',bg='darkseagreen')
            self.ALBlabel1.place(anchor='nw', relheight='0.07', relwidth='1.0', relx='0.0', x='0', y='0')
            self.ALBbooksListbox = tk.Listbox(libraryBooks)
            self.ALBbooksListbox.bind("<<ListboxSelect>>", self.adminLibraryBookListSelect)
            self.ALBbooksListbox.place(anchor='nw', relheight='0.41', relwidth='1.0', relx='0.0', rely='0.09', x='0',
                                       y='0')
            self.ALBlabel2 = tk.Label(libraryBooks)
            self.ALBlabel2.configure(font='{Arial TUR} 13 {}', text='Seçilmiş Kitabın Detayları',bg='lightgrey')
            self.ALBlabel2.place(anchor='nw', relheight='0.05', relwidth='1.0', relx='0.0', rely='0.52', x='0', y='0')
            self.ALBtitleConstLabel = tk.Label(libraryBooks)
            self.ALBtitleConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.ALBtitleConstLabel.configure(font='{Arial TUR} 11 {bold}',text='Başlık:')
            self.ALBtitleConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.05', rely='0.6', x='0',
                                          y='0')
            self.ALBtitleVarLabel = tk.Label(libraryBooks)
            self.ALBtitleVarLabel.configure(anchor='w', cursor='based_arrow_down', font='{Arial TUR} 12 {}',
                                            justify='left')
            self.ALBtitleVarLabel.configure(takefocus=False, text='')
            self.ALBtitleVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.67', relx='0.28', rely='0.6', x='0',
                                        y='0')
            self.ALBauthorConstLabel = tk.Label(libraryBooks)
            self.ALBauthorConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.ALBauthorConstLabel.configure(font='{Arial TUR} 11 {bold}',text='Yazar:')
            self.ALBauthorConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.05', rely='0.67',
                                           x='0', y='0')
            self.ALBauthorVarLabel = tk.Label(libraryBooks)
            self.ALBauthorVarLabel.configure(anchor='w', cursor='based_arrow_down', font='{Arial TUR} 12 {}',
                                             justify='left')
            self.ALBauthorVarLabel.configure(takefocus=False, text='')
            self.ALBauthorVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.67', relx='0.28', rely='0.67',
                                         x='0', y='0')
            self.ALBaddBookButton = tk.Button(libraryBooks)
            self.ALBaddBookButton.configure(text='Kitap Ekle', command=self.buttonShowAddBookAction,bg='grey')
            self.ALBaddBookButton.place(anchor='nw', relwidth='0.3', relx='0.6', rely='0.9', x='0', y='0')
            self.ALBidConstLabel = tk.Label(libraryBooks)
            self.ALBidConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.ALBidConstLabel.configure(font='{Arial TUR} 11 {bold}',text='ID:')
            self.ALBidConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.05', rely='0.74', x='0',
                                       y='0')
            self.ALBidVarLabel = tk.Label(libraryBooks)
            self.ALBidVarLabel.configure(anchor='w', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.ALBidVarLabel.configure(text='')
            self.ALBidVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.25', rely='0.74', x='0',
                                     y='0')
            self.ALBpriceConstLabel = tk.Label(libraryBooks)
            self.ALBpriceConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.ALBpriceConstLabel.configure(font='{Arial TUR} 11 {bold}',text='Fiyat:')
            self.ALBpriceConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.45', rely='0.75',
                                          x='0', y='0')
            self.ALBpriceVarLabel = tk.Label(libraryBooks)
            self.ALBpriceVarLabel.configure(anchor='w', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.ALBpriceVarLabel.configure(text='')
            self.ALBpriceVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.65', rely='0.75', x='0',
                                        y='0')
            self.ALBstockConstLabel = tk.Label(libraryBooks)
            self.ALBstockConstLabel.configure(anchor='e', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.ALBstockConstLabel.configure(font='{Arial TUR} 11 {bold}',text='Stok:')
            self.ALBstockConstLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.05', rely='0.82',
                                          x='0', y='0')
            self.ALBstockVarLabel = tk.Label(libraryBooks)
            self.ALBstockVarLabel.configure(anchor='w', cursor='arrow', font='{Arial TUR} 12 {}', justify='left')
            self.ALBstockVarLabel.configure(text='')
            self.ALBstockVarLabel.place(anchor='nw', relheight='0.04', relwidth='0.2', relx='0.25', rely='0.82', x='0',
                                        y='0')
            self.ALBeditButton = tk.Button(libraryBooks)
            self.ALBeditButton.configure(text='Kitabı Düzenle', command=self.showEditBookFrame,bg='grey')
            self.ALBeditButton.place(anchor='nw', relwidth='0.3', relx='0.1', rely='0.9', x='0', y='0')
        self._currentFrames += [self._adminFrames["info"], self._adminFrames["users"], self._adminFrames["userbooks"],
                                self._adminFrames["libbooks"]]
        self.placeFrames13Formation(self._adminFrames["info"], self._adminFrames["users"],
                                    self._adminFrames["userbooks"], self._adminFrames["libbooks"])
        self.updateAdminInfoFrame()
        self.updateAdminLibraryBookList()
        self.updateAdminUserList()
        self.updateAdminUserBorrowedList()

    def showAddBookFrame(self):
        if self._addBookFrame == None:
            self._addBookFrame = addBook = tk.Frame(self.root)
            self.BAFlabel5 = tk.Label(addBook)
            self.BAFlabel5.configure(font='{Arial TUR} 14 {bold}', text='Kitap Ekleme Ekranı')
            self.BAFlabel5.place(anchor='nw', relwidth='0.5', relx='0.25', rely='0.05', x='0', y='0')
            self.BAFtitleLabel = tk.Label(addBook)
            self.BAFtitleLabel.configure(text='Başlık:')
            self.BAFtitleLabel.place(anchor='nw', relheight='0.08', relwidth='0.2', relx='0.08', rely='0.21', x='0',
                                     y='0')
            self.BAFtitleEntry = tk.Entry(addBook)
            self.BAFtitleEntry.place(anchor='nw', relheight='0.08', relwidth='0.52', relx='0.31', rely='0.21', x='0',
                                     y='0')
            self.BAFauthorLabel = tk.Label(addBook)
            self.BAFauthorLabel.configure(text='Yazar:')
            self.BAFauthorLabel.place(anchor='nw', relheight='0.08', relwidth='0.2', relx='0.08', rely='0.36', x='0',
                                      y='0')
            self.BAFauthorEntry = tk.Entry(addBook)
            self.BAFauthorEntry.place(anchor='nw', relheight='0.08', relwidth='0.52', relx='0.31', rely='0.36', x='0',
                                      y='0')
            self.BAFpriceLabel = tk.Label(addBook)
            self.BAFpriceLabel.configure(text='Fiyat:')
            self.BAFpriceLabel.place(anchor='nw', relheight='0.08', relwidth='0.2', relx='0.08', rely='0.51', x='0',
                                     y='0')
            self.BAFpriceEntry = tk.Entry(addBook)
            self.BAFpriceEntry.place(anchor='nw', relheight='0.08', relwidth='0.52', relx='0.31', rely='0.51', x='0',
                                     y='0')
            self.BAFstockLabel = tk.Label(addBook)
            self.BAFstockLabel.configure(text='Stok:')
            self.BAFstockLabel.place(anchor='nw', relheight='0.08', relwidth='0.2', relx='0.08', rely='0.66', x='0',
                                     y='0')
            self.BAFstockEntry = tk.Entry(addBook)
            self.BAFstockEntry.place(anchor='nw', relheight='0.08', relwidth='0.52', relx='0.31', rely='0.66', x='0',
                                     y='0')
            self.BAFaddBookButton = tk.Button(addBook)
            self.BAFaddBookButton.configure(text='Kitabı Ekle', command=self.addBookButtonAction)
            self.BAFaddBookButton.place(anchor='nw', relx='0.75', rely='0.8', x='0', y='0')
            self.BAFcancelButton = tk.Button(addBook)
            self.BAFcancelButton.configure(text='İptal', command=self.buttonCancelAddBookAction)
            self.BAFcancelButton.place(anchor='nw', relx='0.1', rely='0.8', x='0', y='0')
        self.removeCurrentFrames()
        self._currentFrames += [self._addBookFrame]
        self.placeFrameCenter(self._addBookFrame, 300, 500)

    def showEditBookFrame(self):
        if self._editBookFrame == None:
            self._editBookFrame = editBook = tk.Frame(self.root)
            self.EBFlabel5 = tk.Label(editBook)
            self.EBFlabel5.configure(font='{Arial TUR} 14 {bold}', text='Kitap Düzeltme Ekranı')
            self.EBFlabel5.place(anchor='nw', relwidth='0.5', relx='0.05', rely='0.05', x='0', y='0')
            self.EBFidLabel = tk.Label(editBook)
            self.EBFidLabel.configure(font='{Arial TUR} 11 {bold}', text='ID: ss')
            self.EBFidLabel.place(anchor='nw', relwidth='0.22', relx='0.62', rely='0.05', x='0', y='0')
            self.EBFtitleLabel = tk.Label(editBook)
            self.EBFtitleLabel.configure(text='Başlık:')
            self.EBFtitleLabel.place(anchor='nw', relheight='0.08', relwidth='0.2', relx='0.08', rely='0.21', x='0',
                                     y='0')
            self.EBFtitleEntry = tk.Entry(editBook)
            self.EBFtitleEntry.place(anchor='nw', relheight='0.08', relwidth='0.52', relx='0.31', rely='0.21', x='0',
                                     y='0')
            self.EBFauthorLabel = tk.Label(editBook)
            self.EBFauthorLabel.configure(text='Yazar:')
            self.EBFauthorLabel.place(anchor='nw', relheight='0.08', relwidth='0.2', relx='0.08', rely='0.36', x='0',
                                      y='0')
            self.EBFauthorEntry = tk.Entry(editBook)
            self.EBFauthorEntry.place(anchor='nw', relheight='0.08', relwidth='0.52', relx='0.31', rely='0.36', x='0',
                                      y='0')
            self.EBFpriceLabel = tk.Label(editBook)
            self.EBFpriceLabel.configure(text='Fiyat:')
            self.EBFpriceLabel.place(anchor='nw', relheight='0.08', relwidth='0.2', relx='0.08', rely='0.51', x='0',
                                     y='0')
            self.EBFpriceEntry = tk.Entry(editBook)
            self.EBFpriceEntry.place(anchor='nw', relheight='0.08', relwidth='0.52', relx='0.31', rely='0.51', x='0',
                                     y='0')
            self.EBFstockLabel = tk.Label(editBook)
            self.EBFstockLabel.configure(text='Stok:')
            self.EBFstockLabel.place(anchor='nw', relheight='0.08', relwidth='0.2', relx='0.08', rely='0.66', x='0',
                                     y='0')
            self.EBFstockEntry = tk.Entry(editBook)
            self.EBFstockEntry.place(anchor='nw', relheight='0.08', relwidth='0.52', relx='0.31', rely='0.66', x='0',
                                     y='0')
            self.EBFsubmitEditButton = tk.Button(editBook)
            self.EBFsubmitEditButton.configure(text='Değişiklikleri Gönder', command=self.editBookButtonAction)
            self.EBFsubmitEditButton.place(anchor='nw', relx='0.7', rely='0.8', x='0', y='0')
            self.EBFcancelButton = tk.Button(editBook)
            self.EBFcancelButton.configure(text='İptal', command=self.buttonCancelAddBookAction)
            self.EBFcancelButton.place(anchor='nw', relx='0.1', rely='0.8', x='0', y='0')
        self.removeCurrentFrames()
        self._currentFrames += [self._editBookFrame]
        self.placeFrameCenter(self._editBookFrame, 300, 500)

    ### DATA UPDATE FUNCTIONS ###
    def updateAdminInfoFrame(self):
        info = self.business.getLibraryInfo()
        self.AIFusernameVarLabel.configure(text=info.username)
        self.AIFusernamePanelVarLabel.configure(text=info.username)
        self.AIFcustomerCountVarLabel.configure(text=info.customerCount)
        self.AIFbookCountVarLabel.configure(text=info.bookCount)

    def updateAdminLibraryBookFields(self, bookInfo):
        self.ALBtitleVarLabel.configure(text=bookInfo.title)
        self.ALBauthorVarLabel.configure(text=bookInfo.author)
        self.ALBidVarLabel.configure(text=bookInfo.id)
        self.ALBpriceVarLabel.configure(text=str(bookInfo.price) + " TL")
        self.ALBstockVarLabel.configure(text=bookInfo.stock)

    def updateAdminBorrowedBookFields(self, bookInfo):
        self.AUBtitleVarLabel.configure(text=bookInfo.title)
        self.AUBauthorVarLabel.configure(text=bookInfo.author)
        self.AUBidVarLabel.configure(text=bookInfo.id)
        self.AUBpriceVarLabel.configure(text=str(bookInfo.price) + " TL")
        self.AUBstockVarLabel.configure(text=bookInfo.stock)

    def updateAdminUserFields(self, userData: UserData):
        self.AULusernameVarLabel.configure(text=userData._username)
        self.AULtypeVarLabel.configure(text="Yönetici" if userData._type == 0 else "Müşteri")
        self.AULidVarLabel.configure(text=userData._id)
        self.AULborrowedBooksVarLabel.configure(
            text=len(userData._customer._booksBorrowed) if userData._type != 0 else 0)

    def updateCustomerInfoFrame(self):
        info = self.business.getLibraryInfo()
        self.CIFusernameVarLabel.configure(text=info.username)
        self.CIFusernamePanelVarLabel.configure(text=info.username)
        self.CIFborrowedBookCountVarLabel.configure(text=info.borrowedCount)
        self.CIFcustomerCountVarLabel.configure(text=info.customerCount)
        self.CIFbookCountVarLabel.configure(text=info.bookCount)

    def updateCustomerLibraryBookFields(self, bookInfo):
        self.CLFtitleVarLabel.configure(text=bookInfo.title)
        self.CLFauthorVarLabel.configure(text=bookInfo.author)
        self.CLFidVarLabel.configure(text=bookInfo.id)
        self.CLFpriceVarLabel.configure(text=str(bookInfo.price) + " TL")
        self.CLFstockVarLabel.configure(text=bookInfo.stock)

    def updateCustomerBorrowedBookFields(self, bookInfo):
        self.CBFtitleVarLabel.configure(text=bookInfo.title)
        self.CBFauthorVarLabel.configure(text=bookInfo.author)
        self.CBFidVarLabel.configure(text=bookInfo.id)
        self.CBFriceVarLabel.configure(text=str(bookInfo.price) + " TL")
        self.CBFstockVarLabel.configure(text=bookInfo.stock)

    def updateAdminUserList(self):
        self.AULusersListbox.delete(0, END)
        for user in self.business.data.getUsers():
            self.AULusersListbox.insert(END, user[1])

    def updateAdminLibraryBookList(self):
        self.ALBbooksListbox.delete(0, END)
        for book in self.business.data.getBooks():
            self.ALBbooksListbox.insert(END, book[1])

    def updateAdminUserBorrowedList(self):
        try:
            username = self.AULusersListbox.get(self.AULusersListbox.curselection())
        except:
            username = None
        self.AUBbooksListbox.delete(0, END)
        user = self.business.data.getUser(username)
        if user != None:
            if user._type != 0:
                for book in user._customer.booksBorrowed:
                    self.AUBbooksListbox.insert(END, book._title)

    def updateCustomerLibraryBookList(self):
        self.CLFlistbox1.delete(0, END)
        for book in self.business.data.getBooks():
            self.CLFlistbox1.insert(END, book[1])

    def updateCustomerBorrowedBookList(self):
        self.CBFlistbox1.delete(0, END)
        user = self.business.loggedOnUser
        for book in user._customer.booksBorrowed:
            self.CBFlistbox1.insert(END, book._title)

    ### EVENTS ###
    def adminLibraryBookListSelect(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            title = self.ALBbooksListbox.get(index)
            bookInfo = self.business.data.getBookByTitle(title)
            self.updateAdminLibraryBookFields(bookInfo)

    def adminUserListSelect(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            username = self.AULusersListbox.get(index)
            userInfo = self.business.data.getUser(username)
            self.updateAdminUserFields(userInfo)
            self.updateAdminUserBorrowedList()

    def adminBorrowedBookListSelect(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            title = self.AUBbooksListbox.get(index)
            bookInfo = self.business.data.getBookByTitle(title)
            self.updateAdminBorrowedBookFields(bookInfo)

    def customerLibraryBookListSelect(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            title = self.CLFlistbox1.get(index)
            bookInfo = self.business.data.getBookByTitle(title)
            self.updateCustomerLibraryBookFields(bookInfo)

    def customerBorrowedBookListSelect(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            title = self.CBFlistbox1.get(index)
            bookInfo = self.business.data.getBookByTitle(title)
            self.updateCustomerBorrowedBookFields(bookInfo)

    ### ACTIONS ###
    def logoutButtonAction(self):
        self.business.loggedOnUser = None
        self.showLoginFrame()

    def addBookButtonAction(self):
        title = self.BAFtitleEntry.get()
        author = self.BAFauthorEntry.get()
        price = self.BAFpriceEntry.get()
        stock = self.BAFstockEntry.get()
        try:
            price = int(price)
        except:
            self.warningPopup("Fiyat integer olmalıdır")
            return
        try:
            stock = int(stock)
        except:
            self.warningPopup("Stok integer olmalıdır")
            return
        self.business.data.createBook(title, author, price, stock)
        self.showAdminViewFrames()
        self.updateAdminLibraryBookList()

    def returnBookButtonAction(self):
        try:
            title = self.CBFlistbox1.get(self.CBFlistbox1.curselection())
        except:
            self.warningPopup("Kitap seçilmeli")
            return
        book = self.business.data.getBookByTitle(title)
        self.business.loggedOnUser._customer.returnBookById(book.id)
        self.updateCustomerBorrowedBookList()

    def adminReturnBookButtonAction(self):
        try:
            username = self.AULusersListbox.get(self.AULusersListbox.curselection())
            title = self.AUBbooksListbox.get(self.AUBbooksListbox.curselection())
        except:
            self.warningPopup("Müşteri ve kitap seçilmeli.")
            return
        user = self.business.data.getUser(username)
        book = self.business.data.getBookByTitle(title)
        if user != None:
            user.returnBookById(book.id)
            self.updateAdminUserBorrowedList()

    def editBookButtonAction(self):
        try:
            origtitle = self.ALBbooksListbox.get(self.ALBbooksListbox.curselection())
        except:
            self.warningPopup("Kitap seçilmeli")
            return
        book = self.business.data.getBookByTitle(origtitle)
        id = book.id
        title = self.EBFtitleEntry.get()
        author = self.EBFauthorEntry.get()
        price = self.EBFpriceEntry.get()
        stock = self.EBFstockEntry.get()
        try:
            price = int(price)
        except:
            self.warningPopup("Fiyat integer olmalıdır")
            return
        try:
            stock = int(stock)
        except:
            self.warningPopup("Stok integer olmalıdır")
            return
        self.business.data.updateBook(id, title, author, price, stock)
        self.showAdminViewFrames()
        self.updateAdminLibraryBookList()

    def borrowBookButtonAction(self):
        try:
            title = self.CLFlistbox1.get(self.CLFlistbox1.curselection())
        except:
            self.warningPopup("Kitap seçilmeli")
            return
        book = self.business.data.getBookByTitle(title)
        self.business.loggedOnUser._customer.addBookById(book.id)
        self.updateCustomerBorrowedBookList()

    def buttonShowAddBookAction(self):
        self.showAddBookFrame()

    def buttonShowEditBookAction(self):
        try:
            title = self.ALBbooksListbox.get(self.ALBbooksListbox.curselection())
        except:
            self.warningPopup("Kitap seçilmeli")
            return
        self.showEditBookFrame()
        book = self.business.data.getBookByTitle(title)
        self.EBFidLabel.configure(text="ID: " + book.id)
        self.EBFtitleEntry.delete(0, END)
        self.EBFtitleEntry.insert(0, book.title)
        self.EBFauthorEntry.delete(0, END)
        self.EBFauthorEntry.insert(0, book.author)
        self.EBFpriceEntry.delete(0, END)
        self.EBFpriceEntry.insert(0, str(book.price))
        self.EBFstockEntry.delete(0, END)
        self.EBFstockEntry.insert(0, str(book.stock))

    def buttonCancelAddBookAction(self):
        self.showAdminViewFrames()

    def buttonRegisterAction(self):
        username = self.RFentryUsername.get()
        password = self.RFentryPassword.get()
        accType = 0 if self.RFcheckVar.get() else 1
        if not username.isalnum():
            self.setWarningLabel("Kullanıcı Adı alfanümerik olmalı.")
            return
        user = self.business.attemptRegister(username, password, accType)
        if user == None:
            self.warningPopup("Hata oluştu. Girdiğiniz kullanıcı adı değiştirin")
            return
        self.showLoginFrame()

    def buttonHaveAccAction(self):
        self.showLoginFrame()

    def buttonLoginAction(self):
        username = self.LFentryUsername.get()
        password = self.LFentryPassword.get()
        user = self.business.attemptLogin(username, password)
        if user == None:
            self.setWarningLabel("Kullanıcı adı veya şifre hatalı")
            return
        if user._type == 0:
            self.showAdminViewFrames()
            self.updateAdminInfoFrame()
            self.updateAdminLibraryBookList()
            self.updateAdminUserList()
        else:
            self.showCustomerViewFrames()
            self.updateCustomerInfoFrame()
            self.updateCustomerLibraryBookList()
            self.updateCustomerBorrowedBookList()

    def buttonNoAccAction(self):
        self.showRegisterFrame()


gui = GUI()
gui.root.title("Online Library")
gui.root.iconbitmap('icons/OnlineLibrary.ico')
gui.showLoginFrame()
gui.root.mainloop()