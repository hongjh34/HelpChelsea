
n = int(input())    #입력받은 값을 n변수(테스트 케이스)에 저장한다.


#n번 테스트 케이스 반복
for _ in range(n):
    p = int(input())     #n번째 선수의 수를 입력받아 p변수(선수 수)에 저장한다.
    playerCosts = []     #선수의 가격을 저장할 배열 선언한다.
    playerNames = []     #n번째 선수의 이을을 저장할 배열 선언한다.

    for _ in range(p):  #선수 수만큼 반복
        cost, player = input().split()  #입력받은 값을 공백으로 분리하여 앞문자열은 cost 뒷문자열은 Palyer에 저장한다.

        cost = int(cost)  #앞문자열 cost 숫자로 변환한다.
        playerCosts.append(cost)  #변수 cost playerCosts 배열에 추가한다.
        playerNames.append(player)  #변수 Player playerNames 배열에 추가한다.

    maxIdx = playerCosts.index(max(playerCosts))   #playerCosts 배열에서 최대값의 index를 maxIdx 변수에 저장한다.

    maxPlayerName = playerNames[maxIdx]  #playerNames배열에서 maxIdx의 선수 이름을 maxPlayerName에 저장한다.

    print("최고 연봉 선수는 : " + maxPlayerName)   #maxPlayerName를 출력한다.