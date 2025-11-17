import React, {useState} from 'react';
import {View, Button, Alert, Text} from 'react-native';
import * as Location from 'expo-location';

const BACKEND = 'https://YOUR_CLOUD_RUN_URL';

export default function App(){
  const [status, setStatus] = useState('idle');

  const sendTrigger = async (promptText) => {
    setStatus('getting-location');
    const { status } = await Location.requestForegroundPermissionsAsync();
    if (status !== 'granted') { Alert.alert('Location permission required'); return; }
    const loc = await Location.getCurrentPositionAsync({});
    const body = {
      prompt: promptText,
      user_id: 'user-123',
      name: 'Sathyaa',
      phone: '+91 9025964854',
      latitude: loc.coords.latitude,
      longitude: loc.coords.longitude,
      consent_contact: true
    };
    setStatus('sending');
    try{
      const r = await fetch(`${BACKEND}/trigger`, {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
      const j = await r.json();
      Alert.alert('Response', JSON.stringify(j));
      setStatus('idle');
    }catch(e){
      Alert.alert('Error', e.message);
      setStatus('idle');
    }
  }

  return (
    <View style={{flex:1,justifyContent:'center',alignItems:'center'}}>
      <Text>Guardian Pulse</Text>
      <Button title='Panic: Text (help me)' onPress={() => sendTrigger('help me')} />
      <Button title='Panic: Medical (I am fainting)' onPress={() => sendTrigger('I am fainting')} />
      <Text>Status: {status}</Text>
    </View>
  )
}
