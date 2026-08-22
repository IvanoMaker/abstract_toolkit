class Combination {
    constructor(set) {
        this.set = set;
    }

    isFull() {
        if (this.set.every(item => item === "X")) {
            return "X";
        } else if (this.set.every(item => item === "O")) {
            return "O";
        } else {
            return "#"
        }
    }
}

class Board {
    constructor(rows = 6, cols = 7) {
        this.mtx = Array.from({ length: cols }, () => Array(rows).fill(null));
        this.solutionSet = [];
    }

    updateSolutionSet() {
        this.solutionSet = [];

        // Diagonals
        this.solutionSet.push(new Combination([this.mtx[0][0], this.mtx[1][1], this.mtx[2][2], this.mtx[3][3]]));
        this.solutionSet.push(new Combination([this.mtx[1][1], this.mtx[2][2], this.mtx[3][3], this.mtx[4][4]]));
        this.solutionSet.push(new Combination([this.mtx[2][2], this.mtx[3][3], this.mtx[4][4], this.mtx[5][5]]));
        this.solutionSet.push(new Combination([this.mtx[1][0], this.mtx[2][1], this.mtx[3][2], this.mtx[4][3]]));
        this.solutionSet.push(new Combination([this.mtx[2][1], this.mtx[3][2], this.mtx[4][3], this.mtx[5][4]]));
        this.solutionSet.push(new Combination([this.mtx[3][2], this.mtx[4][3], this.mtx[5][4], this.mtx[6][5]]));
        this.solutionSet.push(new Combination([this.mtx[0][3], this.mtx[1][2], this.mtx[2][1], this.mtx[3][0]]));
        this.solutionSet.push(new Combination([this.mtx[0][4], this.mtx[1][3], this.mtx[2][2], this.mtx[3][1]]));
        this.solutionSet.push(new Combination([this.mtx[0][5], this.mtx[1][4], this.mtx[2][3], this.mtx[3][2]]));
        this.solutionSet.push(new Combination([this.mtx[1][3], this.mtx[2][2], this.mtx[3][1], this.mtx[4][0]]));
        this.solutionSet.push(new Combination([this.mtx[1][4], this.mtx[2][3], this.mtx[3][2], this.mtx[4][1]]));
        this.solutionSet.push(new Combination([this.mtx[1][5], this.mtx[2][4], this.mtx[3][3], this.mtx[4][2]]));
        this.solutionSet.push(new Combination([this.mtx[2][3], this.mtx[3][2], this.mtx[4][1], this.mtx[5][0]]));
        this.solutionSet.push(new Combination([this.mtx[2][4], this.mtx[3][3], this.mtx[4][2], this.mtx[5][1]]));
        this.solutionSet.push(new Combination([this.mtx[2][5], this.mtx[3][4], this.mtx[4][3], this.mtx[5][2]]));
        this.solutionSet.push(new Combination([this.mtx[3][3], this.mtx[4][2], this.mtx[5][1], this.mtx[6][0]]));
        this.solutionSet.push(new Combination([this.mtx[3][4], this.mtx[4][3], this.mtx[5][2], this.mtx[6][1]]));
        this.solutionSet.push(new Combination([this.mtx[3][5], this.mtx[4][4], this.mtx[5][3], this.mtx[6][2]]));

        // Vertical combinations (Columns)
        for (let a = 0; a < 7; a++) {
            this.solutionSet.push(new Combination([this.mtx[a][0], this.mtx[a][1], this.mtx[a][2], this.mtx[a][3]]));
            this.solutionSet.push(new Combination([this.mtx[a][1], this.mtx[a][2], this.mtx[a][3], this.mtx[a][4]]));
            this.solutionSet.push(new Combination([this.mtx[a][2], this.mtx[a][3], this.mtx[a][4], this.mtx[a][5]]));
        }

        // Horizontal combinations (Rows)
        for (let b = 0; b < 6; b++) {
            this.solutionSet.push(new Combination([this.mtx[0][b], this.mtx[1][b], this.mtx[2][b], this.mtx[3][b]]));
            this.solutionSet.push(new Combination([this.mtx[1][b], this.mtx[2][b], this.mtx[3][b], this.mtx[4][b]]));
            this.solutionSet.push(new Combination([this.mtx[2][b], this.mtx[3][b], this.mtx[4][b], this.mtx[5][b]]));
            this.solutionSet.push(new Combination([this.mtx[3][b], this.mtx[4][b], this.mtx[5][b], this.mtx[6][b]]));
        }
    }

    // method for placing a piece, takes the character and the column number (1 INDEXED)
    place(piece, column) {
        if (this.mtx[column][5] != null) {
            return false;
        }

        for (let r = 0; r < 6; r++) {
            if (this.mtx[column][r] == null) {
                this.mtx[column][r] = piece;
                this.updateSolutionSet();
                return true;
            }
        }
        return false;
    }

    // boolean solved function, returns the character who won the game, # if no one has won or the game is tied
    solved() {
        for (const s in this.solutionSet) {
            if (s.isFull() == "O") {
                return s.isFull();
            } else if (s.isFull() == "X") {
                return s.isFull();
            }
        }
        return "#";
    }

    // encode, encode the gameboard for training purposes
    // uses the charMapLst function defined above
    encoded() {
        let mtx = [];
        for (let i = 0; i < 7; i++) {
            mtx.push(charMapLst(this.mtx[i]))
        }
        return mtx.flat();
    }

    // tie, returns true if the gameboard is full and no one has won
    tie() {
        if (this.isFull()) {
            if (this.solved() == "#") {
                return true;
            }
        }
        return false;
    }

    isFull() {
        return this.mtx.every(col => col.every(cell => cell !== null));
    }
}

function charMapLst(l) {
    let r_l = [];
    for (const a in l) {
        if (a == "X") {
            r_l.push(1);
        } else if (a == "O") {
            r_l.push(-1);
        } else {
            r_l.push(0);
        }
    }
    return r_l;
}