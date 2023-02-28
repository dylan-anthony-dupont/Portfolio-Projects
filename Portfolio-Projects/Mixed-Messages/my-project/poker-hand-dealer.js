//---------------------------------------------------------------------------------------------------
// ENTER NUMBER OF PLAYERS BY ASSIGNING A VALUE TO THE VARIABLE 'numPlayers' Below:
//---------------------------------------------------------------------------------------------------
    var numPlayers = 4; // << over here, change the value to whatver you like. See what happens ;)
//---------------------------------------------------------------------------------------------------
//FUNCTION DECLARATIONS: 
//---------------------------------------------------------------------------------------------------
    // player array initialiser function
    function playersFunc(numPlayers){
        let players = [];
        for(let i=1; i<=numPlayers; i++){
            players.push(i)
        }
        return players;
    }

    // player factory function
    function playerFactory(playerNum, card1, card2){
        let player = {
            playerNum, 
            card1, 
            card2
        }
        return player;
    }

    // function to generate random small blind value between 5-50. In multiples of 5.
    function smallBlindGen(){
        const smallBlindVal = (Math.floor(Math.random()*9)*5)+5;
        return smallBlindVal;
    };

    // allocate small blind to random player and big blind (double small) to player next to that player.
    function bothBlindsAllocator(playerArr){
        let range = playerArr.length;
        if(range < 2){
            console.log("There needs to be at least 2 players. Please update your value.");
        }
        else if(range > 22){
            console.log("The theoretical maxiumum number of players to be dealt into a single round of poker using a single deck of cards is 22. Please update your value.");
            console.log("22 players x 2 cards each = 44 cards. 44 + 1 burnt card + 3 cards in the flop + 1 burnt card + 1 turn card + 1 burn card + 1 river card = 52 cards.")
            console.log("More than 22 players would mean a single round could not be possible with a single deck of 52.")
        }
        else{
            let smallBlindPlayerIndex = Math.floor(Math.random()*range);
            let bigBlindPlayerIndex = null;
            if(playerArr[smallBlindPlayerIndex] === playerArr.length){
                bigBlindPlayerIndex = 0;
            }
            else{
                bigBlindPlayerIndex = smallBlindPlayerIndex+1;
            }
            let small = smallBlindGen();
            console.log(`Player ${playerArr[smallBlindPlayerIndex]} is allocated small blind of £${small}.`);
            console.log(`Player ${playerArr[bigBlindPlayerIndex]} is allocated big blind of £${small*2}.`);
        }
    };

    // function to return random card number/figure
    function cardValueGen(){
        const values = ["ACE", 2, 3, 4, 5, 6, 7, 8, 9, 10, "JACK", "QUEEN", "KING"];
        let val = values[Math.floor(Math.random()*13)];
        return val;
    };

    // function to return random card house
    function cardSuitGen(){
        const suits = ["HEARTS", "SPADES", "DIAMONDS", "CLUBS"];
        let suit = suits[Math.floor(Math.random()*4)];
        return suit;
    };

    // factory function to create card object
    function cardFactory(val, suit){
        const card = {
            val,
            suit
        }
        return card;
    };

    // create a function to deal/allocate cards from existing shuffled deck how a dealer would in real life.
    function theDealer(numPlayers){
        let players = [];
        let allocatedCardIndex = 0;
        while(allocatedCardIndex <= numPlayers - 1){
            for(i in playersFunc(numPlayers)){
                let card1 = unallocatedUniqueCards[allocatedCardIndex];
                let card2 = unallocatedUniqueCards[allocatedCardIndex+numPlayers];
                players.push(playerFactory(Number(i)+1, card1, card2));
                allocatedCardIndex++;
            };
        };
        return players;
        } 
//---------------------------------------------------------------------------------------------------
// FUNCTION CALLS:
//---------------------------------------------------------------------------------------------------
    //assign UNIQUE cards to an array. Basically creating and shuffling a deck of 52 cards.
    let unallocatedUniqueCards = [cardFactory(cardValueGen(), cardSuitGen())];
    let uniqueCardCount = 1;
    while(uniqueCardCount <= 51){
        let testCard = cardFactory(cardValueGen(), cardSuitGen());
        let dupCounter = 0;
        for(i=unallocatedUniqueCards.length-1; i>=0; i--){
            if((testCard.suit === unallocatedUniqueCards[i].suit && testCard.val === unallocatedUniqueCards[i].val)){
            dupCounter++;
            }  
        }
        if(dupCounter === 0){
            unallocatedUniqueCards.push(testCard);
            uniqueCardCount++;
        }
    }

    // Allocates small blind to 1 random player and big blind to player next to that player.
        bothBlindsAllocator(playersFunc(numPlayers));

    // Deal cards to players as a dealer would, go around the table first assigning first card to all and then again for the 2nd cards.
        // console.log(unallocatedUniqueCards); // if you'd like to see the whole randomly generated deck printed to the output, uncomment this line.
    if(numPlayers > 1 && numPlayers < 23){
    let players = theDealer(numPlayers);
        // console.log(players); // if you'd like to see the whole array containing all player-objs printed to the output, uncomment this line.
    
    // Finally, print all the players cards to the output
        for(i in players){
            console.log(`Player ${Number(i)+1} was dealt the ${players[i].card1.val} of ${players[i].card1.suit} and the ${players[i].card2.val} of ${players[i].card2.suit}.`);
        }
    }