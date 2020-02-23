//#include "decompositor.h"
#include "OnesMatrix.h"
#include "IntMatrix.h"
#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    // side size of sums matrix (task)
    int size;
    cin >> size;
    IntMatrix sums(size);
    IntMatrix answer(size);
    IntMatrix bigMatrix(size*size);

    // fill all values
    int sum;
    for (int i = 0; i < size*size; ++i) {
        cin >> sum;
        sums.SetValue(i, sum);
    }

    bigMatrix.ComposeMatrix();
    bigMatrix.PrintAsSquare();
    bigMatrix.CascadeRowsSubtraction();
    sums.CascadeSumsSubtraction();
    std::cout << "===Cascaded Matrix===" << std::endl;
    bigMatrix.PrintAsSquare();
    std::cout << "===Cascaded Sums===" << std::endl;
    sums.PrintAsLine();

    for (int row = 0; row < bigMatrix.GetSideSize(); ++row) {
        int foundCol = bigMatrix.ParseBigMatrixRowForSingleAnswer(row);
        if (foundCol >= 0)
        {
            answer.SetValue(foundCol, sums.GetValue(row));
        }
    }

    std::cout << "===Answers 1st iteration===" << std::endl;
    answer.PrintAsSquare();

    return 0;
}
