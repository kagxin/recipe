add a b = a + b
x = 10

myDrop :: Int -> [a] -> [a]
myDrop n xs = if n <= 0 || null xs
              then xs
              else myDrop (n - 1) (tail xs)
isOdd n = mod n 2 == 1

-- lastButOne :: 
lastButOne xs = if length xs <= 2
                then undefined
                else head (drop ((length xs)-2) xs)

lastButOne2 xs = head (drop ((length xs)-2) xs)
data BookInfo = Book Int String [String]
                deriving (Show)

myInfo = Book 9780135072455 "Algebra of Programming"
                ["Richard Bird", "Oege de moor"]
type CustomerID = Int
type ReviewBody = String
data BetterReview = BetterReview BookInfo CustomerID ReviewBody

type CardHolder = String
type CardNumber = String
type Address = [String]
data BillingInfo = CreditCard CardNumber CardHolder Address
                | CashOnDelivery
                | Invoice CustomerID
                deriving (Show)

data Roygbiv = Red
             | Orange
             | Yellow
             | Green
             | Blue
             | Indigo
             | Violet
               deriving (Eq, Show)

sumList (x:xs) = x + sumList xs
sumList [] = 0

bookID      (Book id title authors) = id
bookTitle   (Book id title authors) = title
bookAuthors (Book id title authors) = authors
complicated (True, a, x:xs, 5) = (a, xs)
-- file: ch03/BookStore.hs

nicerID      (Book id _     _      ) = id
nicerTitle   (Book _  title _      ) = title
nicerAuthors (Book _  _     authors) = authors
