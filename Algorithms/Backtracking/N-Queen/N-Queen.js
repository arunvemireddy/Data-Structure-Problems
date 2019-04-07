function Queen(x, y) {
    this.x = x;
    this.y = y;
}

function QueenGame(n, debug) {

    if(n == 2 || n==3){
        return 'NO SOLUTION';
    }

    this.queens = [];
    this.createEmptyBoard = (n) => {
        board = [];
        for (var i = 0; i < n; i++) {
            var row = [];
            for (var k = 0; k < n; k++) {
                row.push(0);
            }
            board.push(row);
        }
        return board;
    }
    this.board = this.createEmptyBoard(n);

    this.insertQueen = (x, y) => {
        if (x >= this.board.length || y >= this.board.length) {
            return false;
        }

        var queen = new Queen(x, y);
        if (debug) {
            console.warn(`trying to insert queen at [${queen.x}][${queen.y}]`)
        }
        if (this.isSafe(queen)) {
            this.queens.push(queen);
            this.board[x][y] = 1;
            if (debug) {
                console.error(`inserted queen at [${queen.x}][${queen.y}]`)
            }
            return true;
        }
        return false;
    }
    this.removeLastQueen = function () {
        if (this.queens.length) {
            let queen = this.queens.pop();
            this.board[queen.x][queen.y] = 0;
            return queen;
        }
    }

    this.isSafe = (queen) => {
        //check left
        for (let y = queen.y; y >= 0; y--) {
            if (this.board[queen.x][y] == 1) {

                return false;
            }
        }

        //left top diagnol
        for (let x = queen.x, y = queen.y; x >= 0 && y >= 0; x-- , y--) {
            //console.log(x,y,this.board[x][y]);
            if (this.board[x][y] === 1) {

                return false;
            }
        }

        //Left bottom diagnol
        for (let x = queen.x, y = queen.y; x < this.board.length && y >= 0; x++ , y--) {
            if (this.board[x][y] === 1) {

                return false;
            }
        }
        return true;
    }

    this.displayGame = () => {
        console.table(this.board);
    }

    this.main = function (x, y) {
        if (this.queens.length === this.board.length) {
            this.displayGame();
            return true;
        }
        if (this.insertQueen(x, y)) {
            this.main(0, this.queens.length)
        } else {
            if ((x + 1) < this.board.length) {
                this.main(x + 1, y);
            } else {
                let lastQueen = this.removeLastQueen();
                if (debug) {
                    console.warn(`removing queen at [${lastQueen.x}][${lastQueen.y}] `)
                }
                this.main(lastQueen.x + 1, lastQueen.y)
            }
        }
    }
    this.main(0, 0);
}

console.time('start')
var game = new QueenGame(8);
console.timeEnd('start');

