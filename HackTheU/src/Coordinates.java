public class Coordinates {

        int x;
        int y;

        public Coordinates(int x, int y) {
            this.x = x;
            this.y = y;
        }

    @Override
    public String toString() {
        return "(" + this.x + "," + this.y + ")";
    }
}
