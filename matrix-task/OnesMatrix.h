/*
 *  Matrix only with -1, 0, +1
 *  The goal is effective memory usage
 */

#pragma once
#include <vector>

class OnesMatrix
{
public:   
    OnesMatrix(int size); // unsquared value (rows or cols, but not rows*cols)!!
    ~OnesMatrix() = default;

    int GetValue(int row, int col);
    void SetValue(int row, int col, int value);

    int GetSideSize() const { return m_size; }
    int GetTotalSize() const { return m_size*m_size; }

private:
    std::pair<bool, bool> IntToBools(int value) const;
    int BoolsToInt(std::pair<bool, bool> value) const;
    int BoolsToInt(bool value1, bool value2) const;

private:
    int                m_size;
    std::vector<bool>  m_values;
};
