#include "IntMatrix.h"
#include <iostream>
#include <iomanip>
#include <cmath>

IntMatrix::IntMatrix(int size) :
    m_sideSize(size),
    m_values(size*size)
{}

int IntMatrix::GetValue(int linear) const
{
    return m_values[linear];
}

int IntMatrix::GetValue(int row, int col) const
{
    return m_values[row * m_sideSize + col];
}


void IntMatrix::SetValue(int linear, int value)
{
    m_values[linear] = value;
}

void IntMatrix::SetValue(int row, int col, int value)
{
    m_values[row * m_sideSize + col] = value;
}

void IntMatrix::ComposeMatrix()
{
    // side size of big matrix == total size of sums matrix

    // sums-matrix side-size
    int sumsSideSize = std::lround(sqrt(m_sideSize)); // explicit double to int
    int totalSize = GetTotalSize();

    for (int cell = 0; cell < totalSize; ++cell) {
        SetValue(cell, 0);
    }

    for (int row = 0; row < m_sideSize; ++row) {
        SetValue(row, row, 1);  //itself

        if ( row % sumsSideSize != 0 )         { SetValue(row, row-1, 1); }   //left
        if ( (row + 1) % sumsSideSize != 0 )   { SetValue(row, row+1, 1); }   //right
        if ( row - sumsSideSize >= 0 )         { SetValue(row, row-sumsSideSize, 1); } //up
        if ( row + sumsSideSize < m_sideSize ) { SetValue(row, row+sumsSideSize, 1); } //down

        if ( (row - sumsSideSize >= 0) &&
             (row % sumsSideSize != 0) )       { SetValue(row, row-sumsSideSize-1, 1); } //up-left
        if ( (row - sumsSideSize >= 0) &&
             ((row + 1) % sumsSideSize != 0) ) { SetValue(row, row-sumsSideSize+1, 1); } //up-right
        if ( (row + sumsSideSize < m_sideSize) &&
             (row % sumsSideSize != 0) )       { SetValue(row, row+sumsSideSize-1, 1); } //down-left
        if ( (row + sumsSideSize < m_sideSize) &&
             ((row + 1) % sumsSideSize != 0) ) { SetValue(row, row+sumsSideSize+1, 1); } //down-right
    }
}

void IntMatrix::CascadeRowsSubtraction()
{
    for (int row = 1; row < m_sideSize; ++row) {
        for (int col = 0; col < m_sideSize; ++col) {
            SetValue(row, col, GetValue(row, col) - GetValue(row-1, col));
        }
    }
}

void IntMatrix::CascadeSumsSubtraction()
{
    for (int cell = 1; cell < m_sideSize*m_sideSize; ++cell) {
        SetValue(cell, GetValue(cell) - GetValue(cell-1));
    }
}

int IntMatrix::ParseBigMatrixRowForSingleAnswer(int rowIdx)
{
    int cellOfFoundOne = -1;
    for (int cell = rowIdx * m_sideSize; cell < ((rowIdx+1) * m_sideSize - 1); ++cell) {
        if (GetValue(cell) == 1) {
            if ( cellOfFoundOne == -1 ) {
                 cellOfFoundOne = cell;
            }
            else {
                return -1; //found more than one
            }
        }
    }
    if (cellOfFoundOne == -2) { // not found
        return false;
    }
    return cellOfFoundOne % m_sideSize; //col of found answer
}

void IntMatrix::PrintAsSquare()
{
    for (int row = 0; row < m_sideSize; ++row) {
        for (int col = 0; col < m_sideSize; ++col) {
            std::cout << std::setw(2) << GetValue(row, col);
        }
        std::cout << std::endl;
    }
}
void IntMatrix::PrintAsLine()
{
    for (int cell = 0; cell < m_sideSize*m_sideSize; ++cell) {
        std::cout << std::setw(2) << GetValue(cell);
    }
    std::cout << std::endl;
}
