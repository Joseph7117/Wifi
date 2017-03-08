import wifi

class Wifi():

    #Searches for available wifi networks and gives us a list
    @staticmethod
    def Search():
        wifiList = []

        wificells = wifi.Cell.all('wlan0')

        for wificell in wificells:
            wifiList.append(wificell)
        return wifiList

    #Searches from a Search List
    @staticmethod
    def SearchList(ssid):
        wifiList = Wifi.Search()

        for cell in wifiList:
            if cell.ssid == ssid:
                return cell
        return False

    #Get Wifi Networks from a saved List
