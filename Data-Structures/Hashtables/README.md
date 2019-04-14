# Hashing and Hashtables

## What is Hashing?
In data strucutes hashing means to convert any kind of alphanumeric string to a NUMBER. Now with this newly generated number we can retrive and save data.

## Hashtables
A hashtable data structure is an ABT also known as *Dictonary* which helps us to retrive data in O(1) time i.e constant time.<br>
in a hashtable we store data in key and value pairs. And a hash function is used to convert the key to a number/address where the value is situated.<br>
Now what is a Hash Function? A hash function simply put is a function which converts any alphanumeric strong to a number or an address.<br>
For example lets take MOD(%) as a hash function.
we have an empty array of length 10
```
 0  1  2  3  4  5  6  7  8  9
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

and we want to insert 123213, 123234, 435345, 12234327 into the array
123213 % 10 = 3(index of the array)<br>
123234 % 10 = 4<br>
435345 % 10 = 5<br>
134327 % 10 = 7<br>

```
 0  1  2     3      4       5     6    7     8  9
[0, 0, 0, 123213, 123234, 435345, 0, 134327, 0, 0]
```

Now if we want to search if 123234 exists into the array, just take mod 10 and check on that index.<br>
But the problem with this hash function is that there is a change of *collision*, which means 2 number can have same hash what will we do then?<br>

Practially this hash is not that simple, but it is out of scope to know what that is right now.<br>

That hash function gives us O(1) time complexity with hight probability 