class Node:
    def __init__(self, name, artist, duration):
        self.name = name
        self.artist = artist
        self.duration = duration
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_song(self, name, artist, duration):
        new_node = Node(name, artist, duration)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        print(f'Música "{name}" adicionada à playlist!')
    
    def remove_song(self, name):
        current = self.head
        while current:
            if current.name == name:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                print(f'Música "{name}" removida da playlist!')
                return
            current = current.next
        print(f'Música "{name}" não encontrada na playlist!')
    
    def move_song(self, name, position):
        current = self.head
        song_to_move = None
        while current:
            if current.name == name:
                song_to_move = current
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                break
            current = current.next
        
        if song_to_move:
            self.insert_song_at_position(song_to_move, position)
            print(f'Música "{name}" movida para a posição {position}!')
    
    def insert_song_at_position(self, song, position):
        current = self.head
        if position == 1: 
            song.next = self.head
            if self.head:
                self.head.prev = song
            self.head = song
            if not self.tail:
                self.tail = song
            return
        
        count = 1
        while current and count < position - 1:
            current = current.next
            count += 1
        
        if current:
            song.next = current.next
            song.prev = current
            if current.next:
                current.next.prev = song
            current.next = song
            if not song.next:
                self.tail = song
    
    def list_songs(self):
        current = self.head
        index = 1
        while current:
            print(f"{index}. {current.name} - {current.artist} - {current.duration}")
            current = current.next
            index += 1
    
    def activate_repeat_mode(self):
        if self.head and self.tail:
            self.tail.next = self.head
            self.head.prev = self.tail
            print("Modo de repetição ativado!")
    
    def deactivate_repeat_mode(self):
        if self.head and self.tail:
            self.tail.next = None
            self.head.prev = None
            print("Modo de repetição desativado!")
    
    def next_song(self, current_song):
        if current_song and current_song.next:
            return current_song.next
        return None
    
    def previous_song(self, current_song):
        if current_song and current_song.prev:
            return current_song.prev
        return None

def menu():
    playlist = Playlist()
    current_song = None
    repeat_mode = False
    
    while True:
        print("\n--- MENU ---")
        print("1. Adicionar música")
        print("2. Remover música")
        print("3. Mover música")
        print("4. Listar músicas")
        print("5. Ativar modo de repetição")
        print("6. Desativar modo de repetição")
        print("7. Avançar para a próxima música")
        print("8. Retroceder para a música anterior")
        print("9. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            name = input("Nome da música: ")
            artist = input("Artista: ")
            duration = input("Duração (ex: 5:30): ")
            playlist.add_song(name, artist, duration)
        
        elif choice == '2':
            name = input("Nome da música a ser removida: ")
            playlist.remove_song(name)
        
        elif choice == '3':
            name = input("Nome da música a ser movida: ")
            position = int(input("Nova posição: "))
            playlist.move_song(name, position)
        
        elif choice == '4':
            print("\n--- Playlist Atual ---")
            playlist.list_songs()
        
        elif choice == '5':
            playlist.activate_repeat_mode()
            repeat_mode = True
        
        elif choice == '6':
            playlist.deactivate_repeat_mode()
            repeat_mode = False
        
        elif choice == '7':
            if not current_song:
                current_song = playlist.head
            else:
                current_song = playlist.next_song(current_song)
                if repeat_mode and not current_song:
                    current_song = playlist.head
            if current_song:
                print(f"Reproduzindo agora: {current_song.name} - {current_song.artist}")
            else:
                print("Nenhuma música na playlist!")
        
        elif choice == '8':
            if not current_song:
                current_song = playlist.head
            else:
                current_song = playlist.previous_song(current_song)
                if repeat_mode and not current_song:
                    current_song = playlist.tail
            if current_song:
                print(f"Reproduzindo agora: {current_song.name} - {current_song.artist}")
            else:
                print("Nenhuma música na playlist!")
        
        elif choice == '9':
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

menu()
