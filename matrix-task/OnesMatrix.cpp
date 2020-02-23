#include "OnesMatrix.h"

OnesMatrix::OnesMatrix(int size) :
    m_size(size),
    m_values(2 * size * size) //2 bits for each value
{}

std::pair<bool, bool> OnesMatrix::IntToBools(int value) const
{
    if (value == 0) { return std::make_pair<bool, bool>(0,0); }
    else if (value == 1) { return std::make_pair<bool, bool>(0,1); }
    else if (value == -1) { return std::make_pair<bool, bool>(1,0); }
    else { return std::make_pair<bool, bool>(1,1); }
}

int OnesMatrix::BoolsToInt(std::pair<bool, bool> value) const
{
    return BoolsToInt(value.first, value.second);
}

int OnesMatrix::BoolsToInt(bool value1, bool value2) const
{
    if (value1 == 0)
    {
        if (value2 == 0) { return 0; }
        else if (value2 == 1) { return 1; }
        else { return 91; }
    }
    else if (value1 == 1)
    {
        if (value2 == 0) { return -1; }
        else { return 92; }
    }
    else { return 93; }
}

int OnesMatrix::GetValue(int row, int col)
{
    int idx = row * m_size + col;
    return BoolsToInt(m_values[idx], m_values[idx+1]);
}

void OnesMatrix::SetValue(int row, int col, int value)
{
    int idx = row * m_size + col;
    std::pair<bool, bool> valuePair = IntToBools(value);
    m_values[idx] = valuePair.first;
    m_values[idx+1] = valuePair.second;
}
