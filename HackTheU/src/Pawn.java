import java.util.ArrayList;

public class Pawn extends gamePiece{

    Pawn(String name, int posX, int posY, boolean team) {
        super(name, posX, posY, team);
    }

    @Override
    public int getPosY() {
        return super.getPosY();
    }

    @Override
    public int getPosX() {
        return super.getPosX();
    }

    @Override
    public boolean getTeam() {
        return super.getTeam();
    }

    @Override
    public void setPosY(int posY) {
        super.setPosY(posY);
    }

    @Override
    public void setPosX(int posX) {
        super.setPosX(posX);
    }

    @Override
    public void incrementNumberOfMoves() {
        super.incrementNumberOfMoves();
    }

    @Override
    public int getNumberOfMoves() {
        return super.getNumberOfMoves();
    }

    @Override
    public String toString() {
        return getName();
    }

    /**
     * return all possible moves of a pawn not considering being out of the board or other players
     * @param grid current game state
     * @return list of possible coordinates
     */
    @Override
    public ArrayList<Coordinates> moves(gamePiece[][] grid) {

        ArrayList<Coordinates> possibleMoves = new ArrayList<>();

        int ySwitch;
        if (getTeam()) ySwitch = -1; // white team going up
        else ySwitch = 1; // black team going down

        if (getPosY() + ySwitch >= 0 && getPosY() + ySwitch < 8) { //within bounds
            if (grid[getPosX()][ getPosY() + ySwitch] != null) {
                //pawns cant do crap
            } else {
                possibleMoves.add(new Coordinates(getPosX(), getPosY() + ySwitch));
                if (getNumberOfMoves() == 0 && isEnemy(grid, grid[getPosX()][getPosY() + ySwitch*2])) {
                    possibleMoves.add(new Coordinates(getPosX(), getPosY() + ySwitch * 2)); //special first move jump
                }
            }
        }
        //kill to diagonal left
        if (getPosY() + ySwitch >= 0 && getPosY() + ySwitch < 8 && getPosX() - 1 >= 0 && grid[getPosY() + ySwitch][getPosX() - 1] != null) {
            possibleMoves.add(new Coordinates(getPosX() -1, getPosY() + ySwitch));
        }
        //kill to diagonal right
        if (getPosY() + ySwitch >= 0 && getPosY() + ySwitch < 8 && getPosX() + 1 >= 0 && grid[getPosY() + ySwitch][getPosX() + 1] != null) {
            possibleMoves.add(new Coordinates(getPosX() + 1, getPosY() + ySwitch));
        }


        return possibleMoves;
    }
}