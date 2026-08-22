class Bot {
    constructor(process) {
        this.process = process;
    }

    move(char, board) {
        if (this.process == "rand") {
            let cols = [1, 2, 3, 4, 5, 6, 7];
            let choice = cols[Math.floor(Math.random() * cols.length)];
            let validMove = false;

            while (!validMove) {
                temp = board.place(char, chocie - 1);
                validMove = temp;
                if (!temp) {
                    cols.remove(choice);
                    if (!cols) {
                        return null
                    }
                    choice = cols[Math.floor(Math.random() * cols.length)];
                } else {
                    break;
                }
            }
            return choice;
        }
    }
}