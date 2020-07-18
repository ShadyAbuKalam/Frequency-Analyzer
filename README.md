## Language character frequency analyzer
This simple analyzer supports English and Arabic scripts to get a current representation of relative frequency for each letter.

### Classes
* `EnglishAlphaFrequencyAnalyzer`
* `ArabicAlphaFrequencyAnalyzer`

```Python
# First, import the desired analyzer
from frequency_analyzer import ArabicAlphaFrequencyAnalyzer

# Second, create an instance
analyzer = ArabicAlphaFrequencyAnalyzer()

# Third, feed text to the analyzer
analyzer.process_text("النص المراد تحليله")

# Last, get statistics
# A tuple is returned where the first element is the total number of chars considered in the analysis
# The second element is a dictionary of char/chars group to its relative frequency percentage
total_chars_counted,statistics = analyzer.compute_statistics()

```
### Notes on Arabic analyzer
1. Tashkeel is ignored while parsing.
2. The following characters are grouped
    * 'ا', 'أ', 'إ', 'آ'
    *  'ؤ', 'و'
    *  'ى', 'ي'
    *  'ة', 'ت'
    *  'ء', 'ئ'
