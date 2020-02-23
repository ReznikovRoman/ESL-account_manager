#include "Decompositor.h"
#include <iostream>
#include <iomanip>

Decompositor::Decompositor(int sum, int amount) :
    m_sum(sum),
    m_amount(amount),
    m_decomposition(amount) // size of the vector with values
{
    m_decomposition.back() = m_sum; // {0 0 0 0 N} - smallest possible value
}

size_t Decompositor::SumAtRange(int a, int z)
{
    size_t sum = 0;
    for (size_t i = a; i <= z; ++i)
    {
       sum += m_decomposition[i];
    }
    return sum;
}

void Decompositor::SetZerosAtRange(int a, int z)
{
    for (size_t i = a; i <= z; ++i)
    {
        m_decomposition[i] = 0;
    }
}

void Decompositor::GenNext()
{
    for (int i = m_amount-1; i >= 0; --i)
    {
        if (m_decomposition[0] == m_sum)
        {
            break;
        }
        if (m_decomposition[i] > 0)
        {
            if (m_decomposition[i] == (m_sum - SumAtRange(0, i-1)))
            {
                ++m_decomposition[i-1];
                m_decomposition.back() = m_decomposition[i] - 1;
                SetZerosAtRange(i, m_amount-2);
            }
            else
            {
                ++m_decomposition[i-1];
                --m_decomposition[i];
            }
            break;
        }
    }
}

void Decompositor::Print()
{
    for (int num : m_decomposition)
    {
        std::cout << std::setw(2) << num << ' ';
    }
    std::cout << std::endl;
}
