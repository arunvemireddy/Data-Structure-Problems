function TOH(disks){
    this.disks = disks;
    this.towers = [];

    //This logic is just for Representation 
    this.constructTowers = function(){
        for(let i =0 ;i<3 ;i++){
            let tower = []
            for(let j=0;j<this.disks;j++){
                if(i==0){
                    tower.push(j+1);
                }
                else{
                    tower.push(0);
                }
                
            }
            this.towers.push(tower);
        }
    }
    //This logic is just for Representation
    this.displayTowers = function(){
        var towerRepresentation = "\n";
        for(let i = 0 ;i<this.disks;i++){
            towerRepresentation += `${this.towers[0][i]}|${this.towers[1][i]}|${this.towers[2][i]}\n`;
        }
        console.warn(towerRepresentation);

    }
    this.shiftPeg = function(n,from,to){
        let index = this.towers[to].lastIndexOf(0);
        this.towers[to][index] = n;
        index = this.towers[from].indexOf(n);
        this.towers[from][index] = 0;
        this.displayTowers();
    }
    this.constructTowers();
    this.displayTowers();


    //Rec code for towerOfHanoi
    this.towerOfHanoi = function(n,from,to,aux){
        if(n==1){
            this.shiftPeg(1,from,to);
            return;
        }
        this.towerOfHanoi(n-1,from,aux,to);
        this.shiftPeg(n,from,to)
        this.towerOfHanoi(n-1,aux,to,from);

    }
    this.towerOfHanoi(this.disks,0,2,1);
}
new TOH(3)
