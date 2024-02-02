# pandas-groupby-axis-1
Use case for Pandas' `groupby(axis=1)` (now deprecated: [pandas#51203]), and 2 example workarounds (using 2 and 4 "transpose" operations, resp.)

- [proj.py] shows a simple example of using `groupby(axis=1)`
- [The `tt` branch][tt diff] shows one workaround for the deprecation:
  - Transpose before `.groupby`
  - Transpose logic in the function passed to DataFrameGroupBy.apply
  - Transpose again after `.apply`
- [The `tttt` branch][tttt diff] shows a simpler workaround, but which introduces 4 transpose operations:
  - Transpose before `.groupby`
  - Transpose at the start of the function passed to DataFrameGroupBy.apply
  - Transpose at the end of the function passed to DataFrameGroupBy.apply
  - Transpose again after `.apply`

<details><summary>Input table</summary>

[ytds.csv](ytds.csv)

<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">crashes</th>
      <th colspan="3" halign="left">cyclist</th>
      <th colspan="3" halign="left">driver</th>
      <th colspan="3" halign="left">passenger</th>
      <th colspan="3" halign="left">pedestrian</th>
    </tr>
    <tr>
      <th></th>
      <th>cur_ytd</th>
      <th>prv_end</th>
      <th>prv_ytd</th>
      <th>cur_ytd</th>
      <th>prv_end</th>
      <th>prv_ytd</th>
      <th>cur_ytd</th>
      <th>prv_end</th>
      <th>prv_ytd</th>
      <th>cur_ytd</th>
      <th>prv_end</th>
      <th>prv_ytd</th>
      <th>cur_ytd</th>
      <th>prv_end</th>
      <th>prv_ytd</th>
    </tr>
    <tr>
      <th>county</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Atlantic</th>
      <td>3</td>
      <td>36</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
      <td>17</td>
      <td>1</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>1</td>
      <td>13</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Bergen</th>
      <td>5</td>
      <td>36</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>21</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>3</td>
      <td>12</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Camden</th>
      <td>3</td>
      <td>41</td>
      <td>3</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>19</td>
      <td>1</td>
      <td>0</td>
      <td>7</td>
      <td>2</td>
      <td>3</td>
      <td>11</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Cape May</th>
      <td>0</td>
      <td>7</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Essex</th>
      <td>2</td>
      <td>50</td>
      <td>6</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>23</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
      <td>1</td>
      <td>2</td>
      <td>24</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Gloucester</th>
      <td>1</td>
      <td>33</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>22</td>
      <td>2</td>
      <td>0</td>
      <td>7</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Hudson</th>
      <td>2</td>
      <td>25</td>
      <td>2</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>11</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>10</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Hunterdon</th>
      <td>1</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Mercer</th>
      <td>2</td>
      <td>31</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>16</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Middlesex</th>
      <td>6</td>
      <td>62</td>
      <td>8</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
      <td>32</td>
      <td>5</td>
      <td>2</td>
      <td>9</td>
      <td>0</td>
      <td>4</td>
      <td>21</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Monmouth</th>
      <td>5</td>
      <td>38</td>
      <td>5</td>
      <td>0</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>3</td>
      <td>7</td>
      <td>0</td>
      <td>2</td>
      <td>9</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Morris</th>
      <td>0</td>
      <td>22</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>14</td>
      <td>1</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Ocean</th>
      <td>6</td>
      <td>41</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>28</td>
      <td>2</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>4</td>
      <td>8</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Passaic</th>
      <td>1</td>
      <td>24</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>15</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>9</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Union</th>
      <td>1</td>
      <td>34</td>
      <td>5</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>3</td>
      <td>0</td>
      <td>6</td>
      <td>1</td>
      <td>1</td>
      <td>15</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Warren</th>
      <td>0</td>
      <td>12</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Burlington</th>
      <td>3</td>
      <td>34</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>26</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Cumberland</th>
      <td>1</td>
      <td>20</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Salem</th>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Somerset</th>
      <td>0</td>
      <td>22</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>14</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Sussex</th>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</details>

<details><summary>Output table</summary>

[proj.csv](proj.csv)

<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="2" halign="left">crashes</th>
      <th colspan="2" halign="left">cyclist</th>
      <th colspan="2" halign="left">driver</th>
      <th colspan="2" halign="left">passenger</th>
      <th colspan="2" halign="left">pedestrian</th>
    </tr>
    <tr>
      <th></th>
      <th>roy</th>
      <th>projected</th>
      <th>roy</th>
      <th>projected</th>
      <th>roy</th>
      <th>projected</th>
      <th>roy</th>
      <th>projected</th>
      <th>roy</th>
      <th>projected</th>
    </tr>
    <tr>
      <th>county</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Atlantic</th>
      <td>33</td>
      <td>36</td>
      <td>2</td>
      <td>2</td>
      <td>17</td>
      <td>19</td>
      <td>6</td>
      <td>6</td>
      <td>11</td>
      <td>12</td>
    </tr>
    <tr>
      <th>Bergen</th>
      <td>39</td>
      <td>44</td>
      <td>1</td>
      <td>1</td>
      <td>21</td>
      <td>23</td>
      <td>4</td>
      <td>4</td>
      <td>10</td>
      <td>13</td>
    </tr>
    <tr>
      <th>Camden</th>
      <td>38</td>
      <td>41</td>
      <td>5</td>
      <td>5</td>
      <td>16</td>
      <td>16</td>
      <td>5</td>
      <td>5</td>
      <td>13</td>
      <td>16</td>
    </tr>
    <tr>
      <th>Cape May</th>
      <td>5</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Essex</th>
      <td>41</td>
      <td>43</td>
      <td>2</td>
      <td>2</td>
      <td>20</td>
      <td>20</td>
      <td>4</td>
      <td>4</td>
      <td>19</td>
      <td>21</td>
    </tr>
    <tr>
      <th>Gloucester</th>
      <td>30</td>
      <td>31</td>
      <td>1</td>
      <td>1</td>
      <td>19</td>
      <td>20</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Hudson</th>
      <td>23</td>
      <td>25</td>
      <td>3</td>
      <td>3</td>
      <td>10</td>
      <td>11</td>
      <td>3</td>
      <td>3</td>
      <td>9</td>
      <td>10</td>
    </tr>
    <tr>
      <th>Hunterdon</th>
      <td>3</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Mercer</th>
      <td>33</td>
      <td>35</td>
      <td>0</td>
      <td>0</td>
      <td>16</td>
      <td>18</td>
      <td>3</td>
      <td>3</td>
      <td>10</td>
      <td>10</td>
    </tr>
    <tr>
      <th>Middlesex</th>
      <td>53</td>
      <td>59</td>
      <td>2</td>
      <td>2</td>
      <td>26</td>
      <td>28</td>
      <td>10</td>
      <td>12</td>
      <td>19</td>
      <td>23</td>
    </tr>
    <tr>
      <th>Monmouth</th>
      <td>33</td>
      <td>38</td>
      <td>3</td>
      <td>3</td>
      <td>17</td>
      <td>18</td>
      <td>9</td>
      <td>12</td>
      <td>5</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Morris</th>
      <td>18</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>12</td>
      <td>4</td>
      <td>4</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Ocean</th>
      <td>41</td>
      <td>47</td>
      <td>1</td>
      <td>1</td>
      <td>26</td>
      <td>28</td>
      <td>6</td>
      <td>6</td>
      <td>9</td>
      <td>13</td>
    </tr>
    <tr>
      <th>Passaic</th>
      <td>23</td>
      <td>24</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>13</td>
      <td>1</td>
      <td>1</td>
      <td>9</td>
      <td>10</td>
    </tr>
    <tr>
      <th>Union</th>
      <td>27</td>
      <td>28</td>
      <td>2</td>
      <td>2</td>
      <td>9</td>
      <td>9</td>
      <td>5</td>
      <td>5</td>
      <td>12</td>
      <td>13</td>
    </tr>
    <tr>
      <th>Warren</th>
      <td>10</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>7</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Burlington</th>
      <td>34</td>
      <td>37</td>
      <td>1</td>
      <td>1</td>
      <td>26</td>
      <td>28</td>
      <td>4</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Cumberland</th>
      <td>19</td>
      <td>20</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>12</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Salem</th>
      <td>10</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>7</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Somerset</th>
      <td>20</td>
      <td>20</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>13</td>
      <td>4</td>
      <td>4</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Sussex</th>
      <td>5</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>5</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</details> 


[pandas#51203]: https://github.com/pandas-dev/pandas/issues/51203
[proj.py]: proj.py
[DataFrameGroupBy.apply]: https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.apply.html
[tt diff]: https://github.com/ryan-williams/pandas-groupby-axis-1/commit/tt
[tttt diff]: https://github.com/ryan-williams/pandas-groupby-axis-1/commit/tttt