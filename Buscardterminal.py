import time

class Card:
    def __init__(self, uid, balance):
        self.uid = uid
        self.balance = balance

class CardDB:
    def __init__(self):
        self.cards = {}

    def register_card(self, card):
        self.cards[card.uid] = card

    def get_card(self, uid):
        return self.cards.get(uid)

    def deduct_balance(self, uid, amount):
        card = self.get_card(uid)
        if card and card.balance >= amount:
            card.balance -= amount
            return True, card.balance
        return False, card.balance if card else 0

class Server:
    def __init__(self, card_db):
        self.card_db = card_db

    def process_fare(self, uid, fare):
        print("서버: 카드 잔액 확인 중...")
        time.sleep(0.5)
        success, new_balance = self.card_db.deduct_balance(uid, fare)
        return success, new_balance

class Terminal:
    def __init__(self, server):
        self.server = server

    def scan_card(self, card):
        print(f"단말기: 카드 인식됨 (UID: {card.uid})")
        print("단말기: 요금 정산 요청 중...")
        fare = 1200  # 기본 요금
        success, new_balance = self.server.process_fare(card.uid, fare)
        if success:
            print(f"단말기: 요금 결제 성공. 남은 잔액: {new_balance}원")
        else:
            print("단말기: 잔액 부족. 승차 불가.")

# 시뮬레이션 시작
db = CardDB()
card1 = Card(uid="1234567890", balance=5000)
db.register_card(card1)

server = Server(card_db=db)
terminal = Terminal(server=server)

print("승객이 카드를 태깅합니다.")
terminal.scan_card(card1)