from playwright.sync_api import expect

ANDROID_APK_VERSION = "Pochtomats-1.2.2-268-production-release.apk"


class Assertions:

    @staticmethod
    def check_apk_file_version(filename: str):
        assert filename == ANDROID_APK_VERSION, (f'Ожидалась версия {ANDROID_APK_VERSION}, '

                                                 f'скачена {filename}')

    @staticmethod
    def check_entered_value(expected_value: str, entered_value: str):
        assert expected_value == entered_value, f"Ожидалось'{expected_value}', получено '{entered_value}'"
