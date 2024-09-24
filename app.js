import React, { useState } from 'react';
import { View, Text, Button, FlatList } from 'react-native';
import axios from 'axios';

const App = () => {
  const [transactions, setTransactions] = useState([]);

  const fetchTransactions = async () => {
    try {
      const response = await axios.post('http://localhost:5000/transactions', {
        access_token: 'your_access_token_here',
      });
      setTransactions(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <View>
      <Button title="Fetch Transactions" onPress={fetchTransactions} />
      <FlatList
        data={transactions}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <Text>{`${item.category}: $${item.amount} on ${item.date}`}</Text>
        )}
      />
    </View>
  );
};

export default App;
