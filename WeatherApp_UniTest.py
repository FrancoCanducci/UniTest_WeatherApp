import unittest
from unittest.mock import patch
import tkinter as tk
from WeatherApp_Python_Previsao import create_app, fetch_weather, widgets

class TestWeatherApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app.update()

    @patch('WeatherApp_Python_Previsao.get_long_term_forecast')
    def test_fetch_weather(self, mock_get_long_term_forecast):
        # Configurar o mock para retornar um resultado simulado
        mock_get_long_term_forecast.return_value = {
            'city': {'name': 'Manaus'},
            'list': [
                {
                    'dt_txt': '2024-06-20 12:00:00',
                    'weather': [{'description': 'céu limpo'}],
                    'main': {'temp': 30.0}
                },
                {
                    'dt_txt': '2024-06-21 12:00:00',
                    'weather': [{'description': 'nublado'}],
                    'main': {'temp': 28.0}
                }
            ]
        }

        # Simular a entrada do usuário
        widgets['city_entry'].insert(0, 'Manaus')

        # Chamar a função fetch_weather
        fetch_weather()

        # Verificar se o resultado foi atualizado corretamente
        result_text = widgets['result_text'].get('1.0', tk.END).strip()
        expected_text = (
            "Previsão do tempo de longo prazo para Manaus:\n\n"
            "Data: 2024-06-20 12:00:00\nCondição: céu limpo\nTemperatura: 30.0°C\n\n"
            "Data: 2024-06-21 12:00:00\nCondição: nublado\nTemperatura: 28.0°C\n\n"
        ).strip()

        print("Resultado esperado:\n", expected_text)
        print("Resultado obtido:\n", result_text)

        self.assertEqual(result_text, expected_text)

if __name__ == '__main__':
    unittest.main(verbosity=2)
