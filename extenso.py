# extenso.py

def extenso(num):
	ret = ''
	nomes_valores = [
		'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
		'sete', 'oito', 'nove',
		'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
		'dezessete', 'dezoito', 'dezenove'
	]
	nomes_dezenas = [
		'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta',
		'setenta', 'oitenta', 'noventa'
	]

	# Checar se o valor passado eh um numero
	if isinstance(num, (int, float)) and num > 0:
		# 3.6 -> 3
		parteInteira = int(num)

		# 3.6 - 3 -> 0.6
		parteDecimal = num - parteInteira

		if parteInteira > 0:
			ret = nomes_valores[parteInteira]

			if parteInteira == 1:
				ret += ' real'
			else:
				ret += ' reais'

		if parteDecimal != 0:
			parteDecimal = int(round(parteDecimal * 100))

			# Adiciona ou nao o '... e centavos'
			if parteInteira > 0:
				ret += ' e '

			if parteDecimal < 20:
				ret += nomes_valores[parteDecimal]

			if parteDecimal >= 20:
				ret += nomes_dezenas[parteDecimal/10 - 2]

			if parteDecimal == 1:
				ret += ' centavo'
			else:
				ret += ' centavos'


		ret = ret.capitalize()

	elif num == 0:
		ret = 'Zero reais'

	else:
		ret = ''

	return ret
