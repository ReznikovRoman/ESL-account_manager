#pragma once
#include <vector>


class IntMatrix
{
public:
    IntMatrix(int size); // unsquared value (rows or cols, but not rows*cols)!!
    ~IntMatrix() = default;

    int GetValue(int linear) const;
    int GetValue(int row, int col) const;

    void SetValue(int linear, int value);
    void SetValue(int row, int col, int value);

    int GetSideSize() const { return m_sideSize; }
    int GetTotalSize() const { return m_sideSize*m_sideSize; }

    // Usage for big_matrix (which has coefficients) only!
    // task logic: center and 8 neigbors (excepted at edges)
    void ComposeMatrix();
    void CascadeRowsSubtraction();
    void CascadeSumsSubtraction();
    int ParseBigMatrixRowForSingleAnswer(int rowIdx);
    // ===================================================

    void PrintAsSquare();
    void PrintAsLine();

private:
    int              m_sideSize;
    std::vector<int> m_values;
};
