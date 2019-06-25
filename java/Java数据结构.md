### Java数据结构

- 秦晋琦 2019年6月

---

### Java数据结构

####  枚举 `Enumeration`

- `nextElement()`方法，返回枚举的下一个元素

#### 位集合 `BitSet`

- ？

#### 向量 `Vector`

向量和传统数组非常相似，但大小可以根据需要动态的改变。

常用方法示例：

```java
import java.util.*;

public class VectorDemo {

   public static void main(String args[]) {
      // initial size is 3, increment is 2
      Vector v = new Vector(3, 2);
      System.out.println("Initial size: " + v.size());
      System.out.println("Initial capacity: " +
      v.capacity());
      v.addElement(new Integer(1));
      v.addElement(new Integer(2));
      v.addElement(new Integer(3));
      v.addElement(new Integer(4));
      System.out.println("Capacity after four additions: " +
          v.capacity());

      v.addElement(new Double(5.45));
      System.out.println("Current capacity: " +
      v.capacity());
      v.addElement(new Double(6.08));
      v.addElement(new Integer(7));
      System.out.println("Current capacity: " +
      v.capacity());
      v.addElement(new Float(9.4));
      v.addElement(new Integer(10));
      System.out.println("Current capacity: " +
      v.capacity());
      v.addElement(new Integer(11));
      v.addElement(new Integer(12));
      System.out.println("First element: " +
         (Integer)v.firstElement());
      System.out.println("Last element: " +
         (Integer)v.lastElement());
      if(v.contains(new Integer(3)))
         System.out.println("Vector contains 3.");
      // enumerate the elements in the vector.
      Enumeration vEnum = v.elements();
      System.out.println("\nElements in vector:");
      while(vEnum.hasMoreElements())
         System.out.print(vEnum.nextElement() + " ");
      System.out.println();
   }
}
```

以上运行的输出为：

```bash
Initial size: 0
Initial capacity: 3
Capacity after four additions: 5
Current capacity: 5
Current capacity: 7
Current capacity: 9
First element: 1
Last element: 12
Vector contains 3.

Elements in vector:
1 2 3 4 5.45 6.08 7 9.4 10 11 12
```

#### 栈 `Stack`

栈是`Vector`的一个子类，它实现了一个标准的后进先出的栈。

堆栈只定义了默认构造函数，用来创建一个空栈。

```java
Stack()
```

因此他除了具有`Vector`的方法，还有自己定义的一些方法。

示例：

```java
import java.util.*;

public class StackDemo {
    static void showpush(Stack<Integer> st, int a) {
        st.push(new Integer(a));
        System.out.println("push(" + a + ")");
        System.out.println("stack: " + st);
    }
    
    static void showpop(Stack<Integer> st) {
        System.out.print("pop -> ");
        Integer a = (Integer) st.pop();
        System.out.println(a);
        System.out.println("stack: " + st);
    }
    
    public static void main(String[] args) {
        Stack<Integer> st = new Stack<Integer>();
        System.out.println("stack: " + st);
        showpush(st, 42);
        showpush(st, 66);
        showpush(st, 99);
        showpop(st);
        showpop(st);
        showpop(st);
        try {
            showpop(st);
        } catch (EmptyStackException e) {
            System.out.println("empty stack");
        }
    }
}
```

#### 字典 `Dictionary`

`Dictionary`是一个抽象类，定义了字典对应的抽象方法

但这个类已经过时了，现在你可以实现Map接口来获取键/值的存储功能。

#### Java Map接口

Map接口中键和值一一映射，可以通过键来获取值。

给定一个键和一个值，你可以将该值存储在一个Map对象，之后通过键来访问对应的值。

```java
import java.util.*;
public class CollectionsDemo {
    public static void main(String[] args) {
        Map m1 = new HashMap();
        m1.put("Zara", "8");
        m1.put("Mahnaz", "31");
        m1.put("Ayan", "12");
        m1.put("Daisy", "14");
        System.out.println();
        System.out.println("Map Elements");
        System.out.print("\t" + m1);
    }
}
```

其涵盖的方法可以完全实现字典数据结构的要求。

#### 哈希表 `Hashtable`

Java2中重构的Hashtable实现了Map接口，因此Hashtable具有从Map接口中定义的方法，还有一些自己的方法。

构造方法：

```java
Hashtable();
Hashtable(int size);
Hashtable(int size, float fillRatio); //指定填充比例
Hashtable(Map m);
```

用法示例：

```java
import java.util.*;

public class HashTableDemo {
    
    public static void main(String[] args) {
        // Create a hash map
        Hashtable balance = new Hashtable();
        Enumeration names;
        String str;
        double bal;
        
        balance.put("Zara", new Double(3434.34));
        balance.put("Mahnaz", new Double(123.22));
        balance.put("Ayan", new Double(1378.00));
        balance.put("Daisy", new Double(-19.08));
        
        //Show all balances in hash table
        names = balance.keys();
        while (names.hasMoreElements()){
            str = (String) names.nextElement();
            System.out.println(str + ": " + balance.get(str));
        }
        System.out.println();
        // Deposit 1,000 into Zara's account
        bal = ((Double) balance.get("Zara")).doubleValue();
        balance.put("Zara", new Double(bal+1000));
        System.out.println("Zara's new balance: " + balance.get("Zara"));
    }
}
```

#### 属性 `Properties`

Properties 继承于 Hashtable.表示一个持久的属性集.属性列表中每个键及其对应值都是一个字符串。

Properties 类被许多Java类使用。例如，在获取环境变量时它就作为System.getProperties()方法的返回值。

示例：

```java
import java.util.*;
 
public class PropDemo {
 
   public static void main(String args[]) {
      Properties capitals = new Properties();
      Set states;
      String str;
      
      capitals.put("Illinois", "Springfield");
      capitals.put("Missouri", "Jefferson City");
      capitals.put("Washington", "Olympia");
      capitals.put("California", "Sacramento");
      capitals.put("Indiana", "Indianapolis");
 
      // Show all states and capitals in hashtable.
      states = capitals.keySet(); // get set-view of keys
      Iterator itr = states.iterator();
      while(itr.hasNext()) {
         str = (String) itr.next();
         System.out.println("The capital of " +
            str + " is " + capitals.getProperty(str) + ".");
      }
      System.out.println();
 
      // look for state not in list -- specify default
      str = capitals.getProperty("Florida", "Not Found");
      System.out.println("The capital of Florida is "
          + str + ".");
   }
}
```





---

#### Q:

- 属性`Properties`和hashtable有什么区别，它是如何被其他类使用的？
- 数据结构更全更详细的，找一些对应的参考书