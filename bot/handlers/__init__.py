from .start import setup_handlers as setup_start_handlers
from .files import setup_handlers as setup_files_handlers

def setup_all_handlers(application):
    """Настройка всех обработчиков"""
    setup_start_handlers(application)
    setup_files_handlers(application)
