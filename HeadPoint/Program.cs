using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;

namespace ConsoleApp
{
    class Program
    {
        static void Main(string[] args)
        {
            List<string> words1 = new List<string>() {"ток", "рост", "кот", "торс", "Кто", "Фывап", "рок"};
            List<string> words2 = new List<string>() {"ток", "ростее", "кота", "торсее", "Кто", "Фывапфафафафафа", "рок"};
            List<string> words3 = new List<string>() {"ток", "ток", "ф", "фа", "ток"};
            List<string> words4 = new List<string>() {"ток"};
            List<string> words5 = new List<string>() {};

            List<List<string>> test1 = new List<List<string>>() { 
                new List<string>{"ток", "кот", "Кто"},  
                new List<string>{"рост", "торс", }, 
                new List<string>{"Фывап" }, 
                new List<string>{"рок" }
            };
            
            List<List<string>> test2 = new List<List<string>>() { 
                new List<string>{"Фывапфафафафафа"}, 
                new List<string>{"ростее", "торсее"},
                new List<string>{"ток", "Кто"},
                new List<string>{"кота" }, 
                new List<string>{"рок" }
            };
            
            List<List<string>> test3 = new List<List<string>>() { 
                new List<string>{"ток", "ток", "ток"},  
                new List<string>{"фа"}, 
                new List<string>{"ф"}
            };
            
            List<List<string>> test4 = new List<List<string>>() { 
                new List<string>{"ток"}
            };
            
            List<List<string>> test5 = new List<List<string>>() { };

            Task task1 = new Task(words1);
            Task task2 = new Task(words2);
            Task task3 = new Task(words3);
            Task task4 = new Task(words4);
            Task task5 = new Task(words5);
            
            task1.TestTask(test1, 1);
            task2.TestTask(test2, 2);
            task3.TestTask(test3, 3);
            task4.TestTask(test4, 4);
            task5.TestTask(test5, 5);
        }
    }

    class Task
    {
        private List<string> _words;
        private List<List<string>> _tree;
        
        public Task(List<string> words)
        {
            _words = words;
            _tree = new List<List<string>>();
        }
        
        public void MakeTree()
        {
            Сalculate();
            BubbleSort();
            //ShowTree();
        }
        
        public void TestTask(List<List<string>> expectTree, int testNumber)
        {
            
            MakeTree();

            if (_tree.Count != expectTree.Count)
            {
                Console.WriteLine("--------");
                Console.WriteLine("Test №" + testNumber + " not passed:");
                Console.WriteLine("Expect:");
                ShowTree(expectTree);
                Console.WriteLine("Result:");
                ShowTree();
                Console.WriteLine("--------");
                return;
            }

            for (int i = 0; i < _tree.Count; i++)
            {
                if (!_tree[i].SequenceEqual(expectTree[i]))
                {
                    Console.WriteLine("--------");
                    Console.WriteLine("Test №" + testNumber + " not passed:");
                    Console.WriteLine("Expect:");
                    ShowTree(expectTree);
                    Console.WriteLine("Result:");
                    ShowTree();
                    Console.WriteLine("--------");
                    return;
                }
            }
            
            Console.WriteLine("--------");
            Console.WriteLine("Test №" + testNumber + " passed:");
            ShowTree();
            Console.WriteLine("--------");
        }
        
        private void Сalculate()
        {
            string firstTempWord;
            string secondTempWord;
            
            for (int i = 0; i < _words.Count; i++)
            {
                firstTempWord = String.Concat(_words[i].OrderBy(c => c)).ToLower();
                _tree.Add(new List<string>()); // новая строка
                _tree[_tree.Count - 1].Add(_words[i]);
                
                for (int j = i + 1; j < _words.Count; j++)
                {
                    if (firstTempWord.Length == _words[j].Length)
                    {
                        secondTempWord = String.Concat(_words[j].OrderBy(c => c)).ToLower();  
                        // сортировка букв в слове по алфавиту

                        if (firstTempWord.Equals(secondTempWord))
                        {
                            _tree[_tree.Count - 1].Add(_words[j]); // новый столбец в строке
                            _words.RemoveAt(j);
                            j--;
                        }
                    }
                }
                
                _words.RemoveAt(i);
                i--;
            }
        }

        private void BubbleSort()
        {
            for(int i = 0; i < _tree.Count; i++)
            {
                for (int j = 0; j < _tree.Count - i - 1; j++)
                {
                    if (_tree[j].Count * _tree[j][0].Length < _tree[j + 1].Count * _tree[j + 1][0].Length)
                    { 
                        (_tree[j], _tree[j + 1]) = (_tree[j + 1], _tree[j]);
                    }
                }
            }
        }

        private void ShowTree()
        {
            foreach (var item in _tree)
            {
                foreach (var words in item)
                {
                    Console.Write(words + " ");
                }
                
                Console.WriteLine();
            }
        }
        
        private void ShowTree(List<List<string>> expectTree)
        {
            foreach (var item in expectTree)
            {
                foreach (var words in item)
                {
                    Console.Write(words + " ");
                }
                
                Console.WriteLine();
            }
        }
    }
}