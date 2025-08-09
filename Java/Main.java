public class Main {

    public static void main(String[] args){
       int age_of_father = 63;
       int age_of_son = 18;
       int Total = age_of_father+age_of_son;
       String nameofson = "Hasanat Ahmad";
       String nameoffather = "Saeed Ahmad";
       String Adalbadal = nameofson.replace(nameofson, nameoffather);
       System.out.println(Adalbadal);
       String name2 = "Ghulu";
       System.out.println(name2.replace("Ghulu", "Ghul"));
       String num = "Apaq Ali Khan";
       System.out.println(num.substring(0,7));


    }
}