import pandas as pd


class AllError(Exception):
    """Общий класс исключения для скриптов"""

    pass


class InstantiateCSVError:
    """Класс исключения для скриптов
    при несоответствии файла необходимым стандартам."""

    def __init__(self, path: str) -> None:
        """
        Инициализация исключения при повреждённом файле.
        """
        self.file_name = path.split("\\")[-1]
        self.path = path

        df = pd.read_csv(path)

        if (len(df.axes[1])) < 3:
            raise AllError(f'{type(self).__name__}: _Файл "{self.file_name}" поврежден_')
