class SimpleSignalGenerator:
    """
        Класс генератора простых сигналов
    """

    def __init__(self, frequency, sampling_frequency, sample_duration, seconds_duration, amplitude):
        """
        Конструктор
        :param frequency: частота (период)
        :param sampling_frequency: частота дискретизации
        :param sample_duration: длительность в сэмплах
        :param seconds_duration: длительность в секундах
        :param amplitude: амплитуда
        """
        pass

    def create_harmonic_signal(self):
        """
        Создает гармонический сигнал
        :return: гармонический сигнал
        """
        pass

    def create_triangular_signal(self):
        """
        Создает треугольный сигнал
        :return: треугольный сигнал
        """
        pass

    def create_pwm_signal(self):
        """
        Создает ШИМ сигнал
        :return: ШИМ сигнал
        """
        pass

    def create_saw_signal(self):
        """
        Создает сигнал пилы
        :return: сигнал пилы
        """
        pass

    def get_signal(self):
        """
        Возвращает сигнал целиком
        :return: сигнал (всю длительность в виде массива)
        """
        pass

    def get_selection(self, sample_number):
        """
        Возвращает выборку сигнала
        :param sample_number: номер сэмпла
        :return: возвращает отдельную выборку сигнала номеру сэмпла или по отметке времени
        """
        pass

    def next_selection(self, selection_length):
        """
        Функция-генератор следующую выборку
        :param selection_length: длина выборки
        :return: следующая выборка сигнала
        """
        pass
