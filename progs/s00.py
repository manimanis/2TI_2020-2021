from time import sleep

print('-' * 5, 'Dark Warez Downloader', '-' * 5)
print('Initializing, please wait... ')
sleep(3)
print('Done.')
print()
print('Welcome to Warez! A service that let you download any game of your '
      'choice')
print()
game = input('Please, input the game name you like ? ')
print('Searching... This operation may take a while...')
sleep(5)
print(game, 'found and ready to download!')
print('This service is provided as is no warranties of any kind are provided.')
answer = input('Do you accept the service conditions ? (Y/n) ')
if answer == 'Y' or answer == 'y':
    print('Downloading...')
    for i in range(100):
        print('Progress ', i, '%', end='\r')
        sleep(0.2)
    print()
    sleep(5)
    print('Network error, retry again!')
else:
    print('Goodbye!')
