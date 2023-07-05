import utils
from url import BASIC_WORD_URL
from players import Player


def main():
    print(f"Ввведите имя игрока")
    user_input = input()
    player = Player(user_input)
    basic_word = utils.load_random_word(BASIC_WORD_URL)

    print(f"Привет, {player.get_word()}!")
    print(f"Составьте {basic_word.count_subwords()} слов из слова {basic_word.get_word()}")
    print(f"Слова должны быть не короче 3 букв")
    print(f"Чтобы закончить игру, угадайте все слова или напишите 'stop'/'стоп'\nПоехали, ваше первое слово?")

    while player.count_subwords() < basic_word.count_subwords():
        player_input = input().lower().strip()

        if player_input in ["stop", "стоп"]:
            break

        elif len(player_input) < 3:
            print("слишком короткое слово")

        elif player.check_words(player_input):
            print("уже использовано")

        elif not basic_word.check_words(player_input):
            print("неверно")

        else:
            player.add_words(player_input)
            print("верно")

    print(f"Игра завершена, вы угадали {player.count_subwords()} слов!")


main()
