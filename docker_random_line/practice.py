import random
from settings import settings
import time
# Напишіть код який раз в delay секунди виводить рядки з
# символів symbol довжиною від min_len до
# max_len(вибрати довжину випадково)


while True:
    time.sleep(settings.delay)
    random_len = random.randint(settings.min_len, settings.max_len)
    print(settings.symbol * random_len)
