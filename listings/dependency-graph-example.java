class A {
  public static void main() {
    B.main();
  }
}

class B {
  public static void main() {
    C.main();
  }
}

class C {
  public static void main() {
    A.main();
  }
}
