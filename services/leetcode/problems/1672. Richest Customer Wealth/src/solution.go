package src

func maximumWealth(accounts [][]int) (maximumWealthNumber int) {

	for _, account := range accounts {
		accountWealth := 0
		for _, amountOfMoney := range account {
			accountWealth += amountOfMoney
		}

		if accountWealth > maximumWealthNumber {
			maximumWealthNumber = accountWealth
		}
	}

	return
}
