from hotel import Hotel
from quarto import Quarto
from cliente import Cliente

hotel = Hotel('Uirapuru', 'Rua Uirapuru')

q1 = Quarto('Suite Master', 2)
q2 = Quarto('Suite Plus', 3)
q3 = Quarto('Suite Single', 1)

hotel.incluir_quarto(q1)
hotel.incluir_quarto(q2)
hotel.incluir_quarto(q3)

cliente1 = Cliente('Fulano', '123')
cliente2 = Cliente('Ciclano', '456')
cliente3 = Cliente('Beltrano', '789')

print(f'Capacidade do Hotel: {len(hotel.quartos)}')
hotel.verificar_disponibilidade()
hotel.reservar_quarto('Suite Master', cliente1)
hotel.reservar_quarto('Suite Plus', cliente2)
hotel.reservar_quarto('Suite Single', cliente3)
hotel.liberar_quarto('Suite Master')
hotel.verificar_disponibilidade()
