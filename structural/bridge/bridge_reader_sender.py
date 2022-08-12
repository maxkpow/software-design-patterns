'''
Example of Bridge pattern.

We need to read data from different sources and
send data via different services.

Pattern Bridge helps to divide abstraction and implementation.
'''

import abc

class IDataReader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self):
        pass

class DatabaseReader(IDataReader):
    def read(self):
        print("Данные из базы данных")

class FileReader(IDataReader):
    def read(self):
        print("Данные из файла")

class ImageReader(IDataReader):
    def read(self):
        print("Данные из картинки")

class Sender(metaclass=abc.ABCMeta):
    
    def __init__(self, data_reader: IDataReader):
        self.reader: IDataReader = data_reader
    
    def set_data_reader(self, data_reader: IDataReader):
        self.reader: IDataReader = data_reader
    
    @abc.abstractmethod
    def send(self):
        pass

class ViberSender(Sender):
    def __init__(self, data_reader: IDataReader):
        super().__init__(data_reader)
    
    def send(self):
        self.reader.read()
        print("Отправлен при помощи Viber")
    

class WhatsAppSender(Sender):
    def __init__(self, data_reader: IDataReader):
        super().__init__(data_reader)
    
    def send(self):
        self.reader.read()
        print("Отправлен при помощи WhatsApp")
    

class EmailSender(Sender):
    def __init__(self, data_reader: IDataReader):
        super().__init__(data_reader)
    
    def send(self):
        self.reader.read()
        print("Отправлен при помощи Email")
    

class TelegramBotSender(Sender):
    def __init__(self, data_reader: IDataReader):
        super().__init__(data_reader)
    
    def send(self):
        self.reader.read()
        print("Отправлен при помощи TelegramBot")


if __name__ == "__main__":
    sender: Sender = EmailSender(DatabaseReader())
    sender.send()

    sender.set_data_reader(FileReader())
    sender.send()
    
    sender = TelegramBotSender(DatabaseReader())
    sender.send()

    sender.set_data_reader(FileReader())
    sender.send()


'''
Without pattern bridge we would have 12 classes:

    ViberSenderFileReader()
    ViberSenderImageReader()
    ViberSenderDatabaseReader()

    WhatsAppSenderFileReader()
    WhatsAppSenderImageReader()
    WhatsAppSenderDatabaseReader()

    TelegramBotSenderFileReader()
    TelegramBotSenderImageReader()
    TelegramBotSenderDatabaseReader()

    EmailSenderDatabaseReader()
    EmailSenderFileReader()
    EmailSenderImageReader()

With applying pattern bridge we have only 7:

    ViberSender()
    WhatsAppSender()
    EmailAppSender()
    TelegramBotAppSender()

    FileReader()
    DatabaseReader()
    ImageReader()
'''