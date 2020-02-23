/*
 *   Decompositor dec(8, 5);
 *   for (size_t i = 1; i <= 299; i++)
 *   {
 *      cout << setw(3) << i << ": ";
 *      dec.Print();
 *      dec.GenNext();
 *   }
 * */

#pragma once
#include <vector>

class Decompositor
{
public:
    Decompositor(int sum, int amount);
    ~Decompositor() = default;

    size_t SumAtRange(int a, int z);
    void SetZerosAtRange(int a, int z);
    void GenNext();
    void Print();

private:
    int              m_sum;
    int              m_amount;
    std::vector<int> m_decomposition;
};
