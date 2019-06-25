## Java类和方法

- 秦晋琦 2019年5月

---

[TOC]

#### 包装类

在实际开发过程中，我们常会遇到需要使用对象，而不是内置数据类型的情况。为了解决这个问题，Java为每一个内置数据类型提供了对应的包装类。

所有的包装类都是抽象类Number的子类。Number类属于java.lang包。

以Character类为例，Character类提供了一系列方法来操纵字符。你可以使用Character的构造方法创建一个Character类对象。

```java
Character ch = new Character('a');
```

将一个char类型的参数传递给需要一个Character类型参数的方法时，那么编译器会自动地将char类型参数转换为Character对象。 这种特征称为**装箱**，反过来称为**拆箱**。

```java
// 原始字符 'a' 装箱到 Character 对象 ch 中
Character ch = 'a';
 
// 原始字符 'x' 用 test 方法装箱
// 返回拆箱的值到 'c'
char c = test('x');
```

#### Java常用类

- Number & Math类
- Character类
- String类
  - String类是不可改变的，如果需要对字符串做修改，应选择使用StringBuffer & StringBuilder类

- StringBuffer & StringBuilder类
  - 和 String 类不同的是，StringBuffer 和 StringBuilder 类的对象能够被多次的修改，并且不产生新的未使用对象。
  - StringBuilder 类在 Java 5 中被提出，它和 StringBuffer 之间的最大不同在于 StringBuilder 的方法不是线程安全的（不能同步访问）。
  - 由于 StringBuilder 相较于 StringBuffer 有速度优势，所以多数情况下建议使用 StringBuilder 类。然而在应用程序要求线程安全的情况下，则必须使用 StringBuffer 类。

#### Java数组

Java语言提供的数组是用来存储固定大小的同类型元素。

##### 数组变量的声明

```java
dataType[] arrayRefVar;
/* example */
double[] myList;
```

##### 创建数组

```java
arrayRefVar = new dataType[arraySize]; //创建数组
dataType[] arrayRefVar = new dataType[arraysize]; //同时声明和创建
dataType[] arrayRefVar = {value0, value1, ... , valuek}; //也可以这样创建
```

##### 多维数组

多维数组可以看成数组的数组：

```java
String str[][] == new String[3][4];
int a[][] = new int[2][3];
```

动态分配：

```java
String s[][] = new String[2][];
s[0] = new String[2]; //为最高维分配引用空间，即限制其能保存的最大长度
s[1] = new String[3];
s[0][0] = new String("Good");
s[0][1] = new String("Luck");
s[1][0] = new String("to");
s[1][1] = new String("you");
s[1][2] = new String("!");
```

##### 数组作为函数的参数

数组可以作为参数传递给方法。如：

```java
public static void printArray(int[] array){
    for (int i = 0; i < array.length; i++) {
        System.out.print(array[i] + " ");
    }
}

/* 调用 */
printArray(new int[] {1,2,3,4,5});
```

##### 数组可以作为函数的返回值

```java
public static int[] reverse(int[] list){
    int[] result = new int[list.length];
    for (int i = 0, j = result.length - 1; i < list.length; i++, j--){
        result[j] = list[i];
    }
    return result;
}
```

上面的实例中result数组作为函数的返回值。

##### Arrays类

`java.util.Arrays`类能方便地操作数组，它提供的所有方法都是静态的。

具有以下功能：

- 给数组赋值：通过`fill`方法
- 对数组排序：`sort`，升序
- 比较数组：`equals`方法
- 查找数组元素：`binarySearch`方法能对排好序的数组进行二分查找。

#### Java日期&时间

`java.util`包提供`Date`类来封装当前的日期和时间。`Date`用来实例化Date对象的构造函数为：

```java
Date(); //使用当前日期和时间来初始化对象
Date(long millisec); //接受一个参数(自1970年1月1日以来的毫秒数)
```

`Date`类还提供了一些可供Date对象调用的方法。实现诸如获取当前日期，日期比较等操作的方法。

##### 使用`SimpleDateFormat`格式化日期

```java
import java.util.*;
import java.text.*;

public class DateDemo {
    public static void main(String args[]) {
        Date dNow = new Date( );
        SimpleDateFormat ft = new SimpleDateFormat ("yyyy-MM-dd hh:mm:ss");
        
        System.out.println("当前时间为：" + ft.format(dNow));
    }
}
```

##### 使用`printf`格式化日期

##### 解析字符串为时间

##### java休眠(sleep)

sleep()函数使当前线程进入停滞状态，让出其霸占的所属进程的CPU资源，留给其他线程执行。

```java
import java.util.*;
public class SleepDemo {
    public static void main(String args[]){
        try{
            System.out.println(new Date() + "\n");
            Thread.sleep(1000*3); //休眠3秒
            System.out.println(new Date() + "\n");
        } catch (Exception e){
            System.out.println("Got an exception!");
        }
    }
}
```

##### 测量时间

```java
import java.util.*;
public class DiffDemo {
 
   public static void main(String args[]) {
      try {
         long start = System.currentTimeMillis(); //起始时间
         System.out.println(new Date( ) + "\n");
         Thread.sleep(5*60*10);
         System.out.println(new Date( ) + "\n");
         long end = System.currentTimeMillis(); //结束时间
         long diff = end - start; //计算差值
         System.out.println("Difference is : " + diff);
      } catch (Exception e) {
         System.out.println("Got an exception!");
      }
   }
}
```

##### `Calendar`类

用于设置和获取日期数据的特定部分，以及相关操作。`Calender`类比`Date`类要强大得多，该抽象类具体使用需要先实现特定的子类的对象，如下:

```java
Calender c = Calender.getInstance(); //默认是当前日期
```

#### Java正则表达式

正则表达式定义了字符串的模式。

正则表达式可以用来搜索、编辑或处理文本。

正则表达式并不仅限于某一种语言，但是在每种语言中有细微差别。

- java正则表达式和Perl的最为相似

#### Java方法

在前面几个章节中我们经常使用到 **System.out.println()**，那么它是什么呢？

- println() 是一个方法。
- System 是系统类。
- out 是标准输出对象。

这句话的用法是调用系统类 System 中的标准输出对象 out 中的方法 println()。

##### 方法的命名规则

- 1.方法的名字的第一个单词应以小写字母作为开头，后面的单词则用大写字母开头写，不使用连接符。例如：**addPerson**。
- 2.下划线可能出现在 JUnit 测试方法名称中用以分隔名称的逻辑组件。一个典型的模式是：**test<MethodUnderTest>_<state>**，例如 **testPop_emptyStack**。

##### 方法的定义

![1559359735920](C:\qin\Notes\java\pics\1559359735920.png)

**注意：** 在一些其它语言中方法指过程和函数。一个返回非void类型返回值的方法称为函数；一个返回void类型返回值的方法叫做过程。

##### 方法的调用

当程序调用一个方法时，程序的控制权交给了被调用的方法。当被调用方法的返回语句执行或者到达方法体闭括号时候交还控制权给程序。

- `main`方法

  - main方法是被JVM调用的。

  - main 方法的头部是不变的，如例子所示，带修饰符 public 和 static,返回 void 类型值，方法名字是 main,此外带个一个 String[] 类型参数。String[] 表明参数是字符串数组。

- void关键字

- 有返回值的函数调用

##### 方法的重载

一个类可以拥有多个相同名字的方法，比如一个是`max(int a1, int a2)`，另一个是`max(double b1, double b2)`，根据传递的参数类型调用不同的方法，这叫做方法重载。

##### 变量作用域

变量的作用范围是程序中该变量可以被引用的部分。方法内定义的变量被称为局部变量。局部变量的作用范围从声明开始，直到包含它的块结束。

##### 命令行参数的使用

命令行传参给main()函数。

##### 构造方法

当一个对象被创建时，构造方法用来初始化该对象。构造方法和它所在类的名字相同，但构造方法没有返回值。

java自动提供一个默认构造方法，一旦你定义了自己的构造方法，默认方法失效。

```java
class MyClass {
    int x;
    
    // 构造函数
    MyClass(int i) {
        x = i;
    }
}
```

接下来调用构造方法初始化对象：

```java
public class ConsDemo {
    public static void main(String[] agrs) {
        MyClass t1 = new MyClass(10);
        MyClass t2 = new MyClass(20);
        System.out.println(t1.x + " " + t2.x);
    }
}
```

##### 可变参数

Java支持传递同类型的可变参数给一个方法。一个方法中只能指定一个可变参数，它必须是方法的最后一个参数，任何普通的参数必须在它之前声明。

```java
public class VarargsDemo {
    public static void main(String[] args) {
        //调用可变参数的方法
        printMax(34,3,3,2,56.4);
        printMax(new double[]{1,2,3});
    }
    
    public static void printMax( double... numbers ){
        if (numbers.length == 0) {
            System.out.println("No argument passed");
            return;
        }
        
        double result = numbers[0];
        
        for (int i = 1; i < numbers.length; i++){
            if (numbers[i] > result) {
                result = numbers[i];
            }
        }
        
        System.out.println("The max value is" + result);
    }
}
```

##### `finalize()`方法

Java的`finalize()`方法在对象被`gc`（垃圾回收器）回收之前调用。

例如，你可以使用`finalize()`方法来确保一个对象打开的文件被关闭了。

在`finalize()`方法中，你必须指定在对象销毁时候要执行的操作。

```java
public class FinalizationDemo{
    public static void main(String[] args){
        Cake c1 = new Cake(1);
        Cake c2 = new Cake(2);
        Cake c3 = new Cake(3);
        
        c2 = c3 = null;
        System.gc(); //调用java垃圾收集器
    }
}

class Cake extends Object {
    private int id;
    public Cake(int id) {
        this.id = id;
        System.out.println("Cake Object" + id + "is created");
    }
    
    protected void finalize() throws java.lang.Throwable {
        // protected是限定符，他确保finalize方法不会被该类以外的代码调用
        super.finalize();
        System.out.println("Cake Object" + id + "is disposed")
    }
}
```

当然，java的内存回收可以由JVM来自动完成，如果你手动使用，可以使用上面的方法。

#### Java流、文件和IO

Java.io 包几乎包含了所有操作输入、输出需要的类。所有这些流类代表了输入源和输出目标。

Java.io 包中的流支持很多种格式，比如：基本类型、对象、本地化字符集等等。

一个流可以理解为一个数据的序列。输入流表示从一个源读取数据，输出流表示向一个目标写数据。

Java 为 I/O 提供了强大的而灵活的支持，使其更广泛地应用到文件传输和网络编程中。

但本节讲述最基本的和流与 I/O 相关的功能。我们将通过一个个例子来学习这些功能。

##### 控制台读取

读取控制台的输入，每次读取单个字符，使用`read()`，按行读取，使用`readLine()`方法。

```java
//read方法举例
import java.io.*;
public class BRRead {
    public static void main(String[] args) throws IOException{
    	char c;
    	// 使用System.in创建BufferedReader
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	System.out.println("输入字符，按下'q'键退出。");
    	// 读取字符
    	do {
    		c = (char) br.read();
    		System.out.println(c);
    	}while (c != 'q');
    }
}
```

##### 控制台输出

控制台的输出由 `print()` 和 `println()` 完成。这些方法都由类 `PrintStream `定义，`System.out` 是该类对象的一个引用。

`System.out.write()`也可以实现输出，但不常用。

##### 读写文件

一个流被定义为一个数据序列。输入流用于从源读取数据，输出流用于向目标写数据。

- `FileInputStream`
- `FileOutputStream`

例子见`C:\qin\Projects\Java\workspace2\test\src\qinjinqi\fileStreamTest & fileStreamTest2`，文件的读写以及二进制乱码问题解决。

##### java中的目录

- `mkdir()/mkdirs()`创建目录

- `isDirectory()`判断一个File对象是不是一个目录

- `list()`提取目录包含的文件和文件夹的列表

- `delete()`方法用于删除空目录或文件，用法示例如下：

  ```java
  package qinjinqi;
  import java.io.File;
  
  public class DeleteFileDemo {
      public static void main(String args[]) {
          // 这里修改为自己的测试目录
          File folder = new File("tmp/java/"); 
          //这里是相对路径，在绝对路径C:\qin\Projects\Java\workspace2\test\下面
          //绝对路径可以使用getProperty()函数进行查询
          deleteFolder(folder);
      }
   
      // 删除文件及目录
      public static void deleteFolder(File folder) {
          File[] files = folder.listFiles();
          if (files != null) {
              for (File f : files) {
                  if (f.isDirectory()) {
                      deleteFolder(f);
                  } else {
                      f.delete();
                  }
              }
          }
          folder.delete();
      }
  }
  ```

#### Java `Scanner`类

#### Java异常处理

要理解Java异常处理是如何工作的，你需要掌握以下三种类型的异常：

- **检查性异常：**最具代表的检查性异常是用户错误或问题引起的异常，这是程序员无法预见的。例如要打开一个不存在文件时，一个异常就发生了，这些异常在编译时不能被简单地忽略。
- **运行时异常：** 运行时异常是可能被程序员避免的异常。与检查性异常相反，运行时异常可以在编译时被忽略。
- **错误：** 错误不是异常，而是脱离程序员控制的问题。错误在代码中通常被忽略。例如，当栈溢出时，一个错误就发生了，它们在编译也检查不到的。

##### 异常和错误

所有的异常类是从 java.lang.Exception 类继承的子类。

![1559464557973](C:\qin\Notes\java\pics\1559464557973.png)

在 Java 内置类中，有大部分常用检查性和非检查性异常。

- 捕获异常

  使用 try 和 catch 关键字可以捕获异常。try/catch 代码块放在异常可能发生的地方。还可以使用多个catch进行多重捕获

- throws/throw关键字

  如果一个方法没有捕获到一个检查性异常，那么该方法必须使用 throws 关键字来声明。throws 关键字放在方法签名的尾部。

  也可以使用 throw 关键字抛出一个异常，无论它是新实例化的还是刚捕获到的。

  一个方法可以声明抛出多个异常，多个异常之间用逗号隔开。

- final关键字

  finally 关键字用来创建在 try 代码块后面执行的代码块。

  无论是否发生异常，finally 代码块中的代码总会被执行。

  在 finally 代码块中，可以运行清理类型等收尾善后性质的语句。

  finally 代码块出现在 catch 代码块最后。

- 注意下面事项：

  - catch 不能独立于 try 存在。
  - 在 try/catch 后面添加 finally 块并非强制性要求的。
  - try 代码后不能既没 catch 块也没 finally 块。
  - try, catch, finally 块之间不能添加任何代码。

##### 声明自定义异常

在 Java 中你可以自定义异常。编写自己的异常类时需要记住下面的几点。

- 所有异常都必须是 Throwable 的子类。
- 如果希望写一个检查性异常类，则需要继承 Exception 类。
- 如果你想写一个运行时异常类，那么需要继承 RuntimeException 类。

##### 通用异常

---

Q:

（1）包装类

（2）装箱和拆箱

（3）java主程序中参数的写法：

```java
public static void main(String []args) {}
public static void main(String args[]) {}
```

哪个常用？

（4）System.out.println/print/printf 这几种print的区别

（5）throws关键字意义

（6）

