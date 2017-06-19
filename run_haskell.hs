run x = zipWith (/) b a
    where b = map (**2) a
          a = map (+1) [0..x]

main = print.last.run $ 2999
